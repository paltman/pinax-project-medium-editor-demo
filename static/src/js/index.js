/* global window document */
window.jQuery = window.$ = require('jquery');

const $ = window.$;

window.Popper = require('popper.js');
require('bootstrap');

import ajaxSendMethod from './ajax';
import MediumEditor from 'medium-editor';
import AutoList from 'medium-editor-autolist';

require('medium-editor-insert-plugin')($);

$(() => {
    $(document).ajaxSend(ajaxSendMethod);

    const imageUploadUrl = $('#id_content').closest('form').data('image-upload-url');

    const editor = new MediumEditor('#id_content', {
        extensions: {
            'autolist': new AutoList()
        },
        toolbar: {
            buttons: [
                'h2',
                'h3',
                'bold',
                'italic',
                'quote',
                'pre',
                'unorderedlist',
                'orderedlist'
            ]
        }
    });

    $('#id_content').mediumInsert({
        editor,
        addons: {
            images: {
                fileUploadOptions: {  // these are options passed to $.ajax; there might be ways for us to pass a function to an option to transform pinax-images data
                    url: imageUploadUrl,
                    acceptFileTypes: /(\.|\/)(gif|jpe?g|png)$/i
                }
            }
        }
    });

    // Topbar active tab support
    $('.topbar li').removeClass('active');

    const classList = $('body').attr('class').split(/\s+/);
    $.each(classList, (index, item) => {
        const selector = `ul.nav li#tab_${item}`;
        $(selector).addClass('active');
    });

    $('#account_logout, .account_logout').click(e => {
        e.preventDefault();
        $('#accountLogOutForm').submit();
    });
});
