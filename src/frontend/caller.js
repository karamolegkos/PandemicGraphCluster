var getResults = function (year, week, num_clusters, callback) {
    var data = {
        year: year,
        week: week,
		num_clusters: parseInt(num_clusters)
    };

    url = 'http://localhost:5000/clusterGraph/';

    // make the request and return the response
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(function (response) {
        callback(response);
    });
}