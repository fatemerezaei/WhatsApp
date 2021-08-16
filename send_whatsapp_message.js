<script>

name = "Jigar Tala" 
 
var mouse = document.createEvent('MouseEvents');
mouse.initEvent(eventName, true, true);
element.dispatchEvent(mouse); 
setTimeout(myFunc, 3000);  
function myFunc()
{
  
    messageBox = document.querySelectorAll("[contenteditable='true']")[1];
    message = "Hello From WhatsApp Automated test!";
    event = document.createEvent("UIEvents");
    messageBox.innerHTML = message.replace(/ /gm, '');
    event.initUIEvent("input", true, true, window, 1);
    messageBox.dispatchEvent(event);

    sendIcon = document.querySelector('span[data-icon="send"]')
    var mouseEvent = document.createEvent("MouseEvents");
    mouseEvent.initMouseEvent
     ('click', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    sendIcon.dispatchEvent(mouseEvent);
    
}    
</script>