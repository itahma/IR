**Project Overview:**
we used to data set :
1- [beir] (https://ir-datasets.com/beir.html#beir/trec-covid)
2- [covid19] (https://ir-datasets.com/cord19.html#cord19/trec-covid/round4)
my project focuses on creating a search engine for two datasets: COVID-19 and BIRE.
The project includes several preprocessing steps, the creation of a TF-IDF matrix, an inverted index, and various enhancements.
**Preprocessing Steps:**
List and describe each preprocessing step :
1. replace_percent_text for replace % with percent
2. expand_country_names usinr packeg pycountry
3. clean_text for Remove punctuations
4. lower_text for Convert to lowercase
5. lemmatize_text using WordNetLemmatizer
6. stem_text using PorterStemmer
7. remove_stopwords using stopwords
8. correct_spelling using TextBlob
**TF-IDF Matrix and Inverted Index:**
calculate tfidf for documints via TfidfVectorizer 
**Query Processing and Representation:**
query is processed and represented using the same steps as in the preprocessing section.
query is tokenized, cleaned, stemmed, and transformed to match the format of the TF-IDF matrix.
**Cosine Similarity Calculation:**
The cosine similarity is a measure that quantifies the similarity between two vectors in a high-dimensional space. In the context of a search engine, it is commonly used to calculate the similarity between a query and documents in the dataset.
**Enhancements:**
enhancement I mentioned (topic algorithm using LatentDirichletAllocation, cluster algorithm using KMeans, query suggestions).
 how each enhancement improves the search engine's performance or user experience:
 Rank the documents based on their cosine similarity values. Higher cosine similarity values indicate higher similarity to the query.
 suggistions:
 

 
 
 
**Evaluation Metrics:**
 the evaluation metrics you calculated (Precision@10, Precision, Recall, MAP, MRR).
 
 

 **Conclusion:**
1.Information Retrieval: The search engine provides a means for users to retrieve relevant documents from the COVID-19 and BIRE datasets based on their queries.     It leverages various techniques to improve retrieval accuracy and efficiency.
2. TF-IDF Matrix and Inverted Index: The project calculates the TF-IDF matrix for the documents in the datasets. This matrix represents the importance of each        term in each document, enabling efficient retrieval based on term relevance. Additionally, the creation of an inverted index allows for quick document     rtrieval based on terms, significantly speeding up the search process.
 
 Overall, the search engine project aims to provide a robust, efficient, and user-friendly solution for information retrieval from the COVID-19 and BIRE datasets. It combines various techniques, algorithms, and evaluation measures to deliver relevant search results and enhance the overall search experience.







 # Flask Search Engine for Information Retrieval System

This application is a search engine for an information retrieval system built using Flask. It supports two datasets and provides functionalities for refining queries, retrieving documents based on queries, and implementing clustering and topic modeling algorithms for enhanced search results.

## Features

- **Refine Query**: Provides query suggestions to help users refine their search.
- **Query Search**: Retrieves documents based on the user's query.
- **Cluster-Based Query Search**: Enhances search results using clustering algorithms.
- **Topic-Based Query Search**: Enhances search results using topic modeling algorithms.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Scipy

### Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Download Datasets and Place in Appropriate Paths**:

    Make sure you have the required datasets and place them in the specified paths in the code.

## Usage

### Running the Application

1. **Set the Dataset**:

    Before running the queries, you need to set the dataset by sending a POST request to `/set_dataset` with the dataset value (`1` or `2`).

    ```sh
    curl -X POST -F 'dataset=1' http://localhost:5000/set_dataset
    ```

2. **Refine Query**:

    Send a POST request to `/refine_query` with the user query to get suggested queries.

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"user_query": "your query"}' http://localhost:5000/refine_query
    ```

3. **Query Search**:

    Send a POST request to `/get_query` with the keyword to retrieve documents.

    ```sh
    curl -X POST -F 'kewword=your keyword' http://localhost:5000/get_query
    ```

4. **Cluster-Based Query Search**:

    Send a POST request to `/get_query_with_cluster` with the keyword to retrieve documents using clustering algorithms.

    ```sh
    curl -X POST -F 'kewword=your keyword' http://localhost:5000/get_query_with_cluster
    ```

5. **Topic-Based Query Search**:

    Send a POST request to `/get_query_with_topic` with the keyword to retrieve documents using topic modeling algorithms.

    ```sh
    curl -X POST -F 'kewword=your keyword' http://localhost:5000/get_query_with_topic
    ```

### Example

Here is an example of how to use the application with `curl`:

1. **Set the Dataset**:

    ```sh
    curl -X POST -F 'dataset=1' http://localhost:5000/set_dataset
    ```

2. **Refine Query**:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"user_query": "machine learning"}' http://localhost:5000/refine_query
    ```

3. **Query Search**:

    ```sh
    curl -X POST -F 'kewword=machine learning' http://localhost:5000/get_query
    ```

## File Structure



.
├── app.py # Main application file.
├── implment_cluster.py # Clustering algorithm implementation.
├── query_processing.py # Query processing logic.
├── implment_topic.py # Topic modeling algorithm implementation.
├── eval.py # Evaluation script for dataset 1.
├── eval2.py # Evaluation script for dataset 2.
├── get_queries.py # Script to retrieve queries.
├── suggistions.py # Script to refine queries.
├── requirements.txt # Python dependencies.
└── README.md # This README file.






## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feel free to reach out.



