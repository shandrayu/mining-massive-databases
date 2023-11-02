from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.feature import StopWordsRemover

def tf_idf(df, input_column_name, num_features, additional_stop_words):
    # Tokenize
    tokenizer = Tokenizer(inputCol=input_column_name, outputCol="tokens")
    with_tokens = tokenizer.transform(df)

    # Remove stop words
    stopwords_filename = "stopwords-en.txt"
    if not os. path. exists(stopwords_filename):
      !wget https://raw.githubusercontent.com/stopwords-iso/stopwords-en/master/stopwords-en.txt


    stop_words = []
    with open(stopwords_filename) as file:
        for line in file:
          stop_words.append(line.rstrip())

    stop_words.extend(additional_stop_words)
    remover = StopWordsRemover(stopWords=stop_words)
    remover.setInputCol("tokens")
    remover.setOutputCol("clean_tokens")
    clean_tokens = remover.transform(with_tokens)

    # Perform TF-IDF
    hashing_tf = HashingTF(inputCol="clean_tokens", outputCol="raw_features", numFeatures=num_features)
    featurized_data = hashing_tf.transform(clean_tokens)

    idf = IDF(inputCol="raw_features", outputCol="vector_space")
    idf_model = idf.fit(featurized_data)
    results = idf_model.transform(featurized_data)

    return results