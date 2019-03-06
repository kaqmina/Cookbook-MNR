$(function() {
    $('#add').on('click', function( e ) {
        e.preventDefault();
        $('<div/>').addClass( 'new-text-div' )
        .html( $('<input type="textbox"/>').addClass( 'someclass' ) )
        .append( $('<button/>').addClass( 'remove' ).text( 'Remove' ) )
        .insertBefore( this );
    });
    $(document).on('click', 'button.remove', function( e ) {
        e.preventDefault();
        $(this).closest( 'div.new-text-div' ).remove();
    });
});

$('.link-formset').formset({
    addText: 'add link',
    deleteText: 'remove'
});

$('#add_more_ing').click(function() {
    var form_idx = $('#id_ingredients-TOTAL_FORMS').val();
    $('#ing_formset').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
    $('#id_ingredients-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});

$('#add_more_stp').click(function() {
    var form_idx = $('#id_steps-TOTAL_FORMS').val();
    $('#stp_formset').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
    $('#id_steps-TOTAL_FORMS').val(parseInt(form_idx) + 1);
});