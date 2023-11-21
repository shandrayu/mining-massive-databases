from sseclient import SSEClient as EventSource
import time
import json


def hash_user(wiki, id):
    return hash((wiki, id))

def fetch_users(event_source, fetching_time_sec, message_types, wikis, event_decimation=5, print_log=False):
    observed_users = set()
    skipped_users = set()
    user_counter = 0
    start_time = time.time()
    for event in event_source:
        try:
            change = json.loads(event.data)
        except:
            # ignore message
            continue

        if change["type"] not in message_types or change["wiki"] not in wikis:
            # ignore message
            continue

        user = hash_user(change["wiki"], change["user"])
        if user in observed_users:
            if print_log:
                print(f"Message from user {user} saved")
            save_user = True
        elif user in skipped_users:
            if print_log:
                print(f"Message from user {user} skipped")
            save_user = False
        else:
            # new user   
            if user_counter % event_decimation == 0:
                if print_log:
                    print(f"+ Add new user {user}")
                observed_users.add(user)
                save_user = True
            else:
                if print_log:
                    print(f"- Add Skip user {user}")
                skipped_users.add(user)
                save_user = False
            user_counter += 1

        elapced_time = time.time() - start_time
        if elapced_time > fetching_time_sec:
            break

        if save_user:
            yield (change)

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
message_types = {"edit"}
wikis = {"enwiki"}#, "wikidatawiki"}
wikis_str = "_".join(wikis)
fetching_time_sec = 10000
changes = [change for change in fetch_users(EventSource(url), fetching_time_sec, message_types, wikis)]

print(f"Collected {len(changes)} edits")

with open(f"changes_{len(changes)}_{wikis_str}_{fetching_time_sec}_sec.json", "w", encoding="utf-8") as json_file:
    json.dump(changes, json_file, ensure_ascii=True, indent=4)