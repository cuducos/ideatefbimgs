$(document).ready(function(){

    $('#color').ColorPicker({
        color: '#0000ff',
        onShow: function (colpkr) {
            $(colpkr).fadeIn(500);
            return false;
        },
        onHide: function (colpkr) {
            $(colpkr).fadeOut(500);
            return false;
        },
        onChange: function (hsb, hex, rgb) {
            $('#color').val('#' + hex);
            preview()
        }
    });

    $('input').change(preview);
    preview()
})

function preview() {

    // load values from form
    v = $('#volume').val();
    y = $('#year').val();
    s = $('#season').val();
    c = $('#color').val();

    // if values are blank, replace by default
    if (v == '') v = Math.floor(Math.random()*41)
    if (y == '') y = $('#year').attr('placeholder');
    if (s == '') s = $('#season').attr('placeholder');
    if (c == '') c = '#0000ff';

    // create image
    p = $('#preview');
    if ($('img', p).length == 0) p.append('<img />');
    img = $('img', p);
    url = create_url(v, y, s, c)
    img.attr('src', url)

}

function create_url(v, y, s, c) {
    base_url = $('form').attr('action');
    url = base_url + '?volume=' + encodeURIComponent(v);
    url = url + '&season=' + encodeURIComponent(s);
    url = url + '&year=' + encodeURIComponent(y);
    url = url + '&color=' + encodeURIComponent(c);
    return url;
}

