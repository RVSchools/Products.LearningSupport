/**
 * Input validation functions for LearningSupport.Request type
 */
function initialize_LST() 
{
    var node = jq("#native");
    if (node) { node.bind('change', change_Native); }
    var node = jq("#fieldsetlegend-request");
    if (node) { node.bind('click', check_Phones); }
    var node = jq("input:radio[name=cfsaCare]");
    if (node) { node.bind('change', check_CFSA); }
    // Now trap the submits...
    var form = jq("#request-base-edit");
    form.bind('submit', check_submit);
};
function change_Native(e) 
{
    var treaty = jq('#archetypes-fieldname-treaty');
    if (e.target.checked) {
        treaty.addClass('error');
        treaty.find('.fieldErrorBox').text('Remember to provide a treaty number.').show();
    } else {
        treaty.removeClass('error');
        treaty.find('.fieldErrorBox').hide();
    }
}
function check_Native() 
{
    var treaty = jq('#archetypes-fieldname-treaty');
    var elem_1 = document.getElementById('native');
    var elem_2 = jq('#treaty');
    if (elem_1.checked) {
        if(elem_2.val()=='') {
            treaty.addClass('error');
            treaty.find('.fieldErrorBox').text('Remember to provide a treaty number.').show();
            focus_schemata_field('student', 'treaty');
            return false;
        } else {
            treaty.removeClass('error');
            treaty.find('.fieldErrorBox').hide();
            return true;
        }
    }
    return true;
}
function check_CFSA(e)
{
    var required = false;
    if (!e) {
        var checkVal = jq('input:radio[name=cfsaCare]:checked').val();
        if (checkVal=='Yes') {
            required = true;
        }
    } else {
        if (e.target.value=='Yes') {
            required = true;
        }
    }
    if (required) {
        msg = "Please enter the social worker's";
        var errorFlag = false;
        if (jq('#cfsaName').val()=='') {set_error('cfsaName', msg+' name.'); errorFlag = true;}
        if (jq('#cfsaPhone').val()=='') {set_error('cfsaPhone', msg+' phone.'); errorFlag = true;}
        if (jq('#cfsaEmail').val()=='') {set_error('cfsaEmail', msg+' email.'); errorFlag = true;}
        if (errorFlag) {
            focus_schemata_field('external-agents', 'cfsaName');
            return false;
        } else {
            return true;
        }
    } else {
        clear_error('cfsaName');
        clear_error('cfsaPhone');
        clear_error('cfsaEmail');
        return true;
    }
}
function check_Phones() 
{
    var home = jq('#g1Phone');
    var work = jq('#g1PhoneWork');
    var cell = jq('#g1PhoneCell');
    if (!home.val() && !work.val() && !cell.val()) {
        var msg = 'You must provide at least one phone number (home, phone, or cell).';
        set_error('g1Phone', msg);
        set_error('g1PhoneWork', msg);
        set_error('g1PhoneCell', msg);

        focus_schemata_field('parents', 'g1Phone');
        return false;
    }
    return true;
}
function check_submit() 
{
    if (!check_Native()) { return false; }
    if (!check_Phones()) { return false; }
    if (!check_CFSA()) { return false; }
    return true;
}
/**
 * UTILITIES 
 */
function clear_error(fldName) 
{
    var el = jq('#archetypes-fieldname-'+fldName);
    el.removeClass('error');
    el.find('.fieldErrorBox').text('');
    document.getElementById(fldName).value='';
}
function set_error(fldName, msg)
{
    var el = jq('#archetypes-fieldname-'+fldName);
    el.addClass('error');
    el.find('.fieldErrorBox').text(msg);
}
function focus_schemata_field(schemata, fldName) 
{
    jq('#fieldsetlegend-'+schemata).click();
    // DOM input focus, not to be confused with jQuery's focus
    document.getElementById(fldName).focus();
}
jq(document).ready(initialize_LST);
