  var ACCESS_TOKEN = '7ZRcKQKFnp+M4xjYtfCSnMukflKpHLVR/CcByVcZZho5ZHbEISqFZJ7y3TNToNAzEBZDYmAYWRK+2BtBHt0NfT1yFtb6bh4d3inwx+BDWVm9iYcmDKwUa9C1hQ8qj25J6k5Jg3MkpBsXfCOykTPdoVGUYhWQfeY8sLGRXgo3xvw=';
var url = 'https://api.line.me/v2/bot/message/reply'; // ������å������Ѥ�API URL
 
/**
 * doPost
 * �桼������LINE�˥�å����������������ν���
 **/
function doPost(e) {
 
    // ��å������ֿ�
    replyMessage(e);
    return ContentService.createTextOutput(JSON.stringify({ content: 'post ok' })).setMimeType(ContentService.MimeType.JSON);
};
 
/**
 * replyMessage
 * ��å��������ֿ�
 **/
var replyMessage = function (e) {

    var replyToken = JSON.parse(e.postData.contents).events[0].replyToken;
    
    UrlFetchApp.fetch(url, {
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            Authorization: 'Bearer ' + ACCESS_TOKEN
        },
        method: 'post',
        payload: JSON.stringify({
            replyToken: replyToken,
            messages: [
                {
                    type: 'text',
                    text: userMessage + '�å���'
                }
            ]
        })
    });
};# line-api
