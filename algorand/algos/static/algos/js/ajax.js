function loadAndDisplayImage(url, containerId) {
    $.ajax({
        url: url,
        method: 'GET',
        xhrFields: {
            responseType: 'blob'
        },
        success: function(data) {
            // Создаем объект URL для полученного Blob
            var imageUrl = URL.createObjectURL(data);

            // Создаем элемент <img> и устанавливаем URL в качестве источника изображения
            var imgElement = $('<img>').attr('src', imageUrl);

            // Вставляем элемент <img> в контейнер
            $('#' + containerId).append(imgElement);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Error:', errorThrown);
        }
    });
}

function graphicShow(url) {
    // Загружаем и отображаем все три PNG-изображения при загрузке страницы
    if (url === '/') {
        var parameters = ['1', '2', '3'];
        var graphicContainer = $('#graphic-container');

        $.each(parameters, function(index, parameter) {
            var graphicUrl = graphic + '?parameter=' + parameter;
            loadAndDisplayImage(graphicUrl, 'graphic-container');
        });
    }
}

$(document).ready(function() {
    graphicShow(window.location.pathname);
});

$(document).on('click', '.menu-link', function(event) {
  event.preventDefault();

  var url = $(this).attr('href');

  $.ajax({
    url: url,
    type: 'GET',
    success: function(data) {

      var content = $(data).find('#content').html();

      $('#content').html(content);
      history.pushState(null, '', url);
      console.log(url);

      graphicShow(url);
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
});