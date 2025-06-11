# Import Libraries
import os
from flask import Flask, request
from flask_cors import CORS

# Import Custom Libraries
from loader import get_normal_data
from clusterer import cluster_data

# Compute the normalised data
print("[INFO | STARTUP] Computing Datasets")
normal_data = get_normal_data()

""" Environment Variables """
# Flask app Host and Port
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 5000))

""" Global variables """
# The name of the flask app
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
 
@app.route('/clusterGraph/', methods=['POST'])
def cluster_graph():
    # Get the data from the request
    data = request.get_json()
    year = data['year'] # String
    week = data['week'] # String
    num_clusters = data['num_clusters']

    # Make Graph and Calculate Clusters
    print("[INFO | CLUSTERING] Clustering Data")
    codes, colors = cluster_data(normal_data, str(year), str(week), int(num_clusters))
  
    answer = {
        "codes" : codes,
        "colors" : colors.tolist()
    }

    print("[INFO | CLUSTERING] Clustering Complete")
    return answer, 200

if __name__ == "__main__":
    # Run the flask app
    print("[INFO | STARTUP] Starting Flask app")
    app.run(HOST, PORT, True, use_reloader=False)