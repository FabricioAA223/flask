function getImages() {
    var interval = document.getElementById('interval').value;
    var duration = document.getElementById('duration').value;

    $.ajax({
        url: '/get_images/' + interval + '/' + duration,
        type: 'GET',
        success: function(response) {
            displayImages(response.images);
        },
        error: function(error) {
            console.error('Error al obtener imágenes:', error);
        }
    });
}

function displayImages(images) {
    var container = document.getElementById('image-container');
    container.innerHTML = '';

    images.forEach(function(imageData) {
        var timestamp = imageData.timestamp;
        var imageBase64 = imageData.image;

        var imageDiv = document.createElement('div');
        imageDiv.innerHTML = '<p>Timestamp: ' + timestamp + '</p>' +
                             '<img src="data:image/jpeg;base64,' + imageBase64 + '" alt="Captured Image">';

        container.appendChild(imageDiv);
    });
}
