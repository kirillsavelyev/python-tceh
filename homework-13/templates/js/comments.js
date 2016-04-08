/**
 * Created by ska on 08.04.16.
 */

'use strict';

(function (window, document, $) {
        function sendComment(comment, post_id) {
            var results = $('.row', '.comments');

            var request = $.ajax({
                url: 'http://127.0.0.1:5000/new_comm/' + post_id,
                type: 'POST',
                //crossDomain: true,
                dataType: 'json',
                data: JSON.stringify(comment, null, '\t')
            });

            request.success(function (data, textStatus, jqXHR) {
                console.log(data, textStatus, jqXHR);
                var result = $('<div>').addClass('col-sm-10').text('????');
                //TODO: insert data.text
                results.append(result);
            });
        }

        $(document).ready(function() {
            var comm = $('#text').val();
            var post_id = $('#post_id').val();
            $('#new_comment').click(function() {
                sendComment(comm, post_id);
            });
        });
    })(window, document, jQuery);

