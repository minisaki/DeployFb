const deviceEl = document.querySelector('#device').textContent
const userEl = document.querySelector('.userName')
const passEl = document.querySelector('.password')
const buttonEl = document.querySelector('#getcookie')
console.log(deviceEl)
const deviceId = JSON.parse(deviceEl);
const connectSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/chat/" + deviceId + "/"
);

buttonEl.addEventListener('click', getcookie)

function getcookie(e) {
    e.preventDefault()
    const userName = userEl.value
    const pass = passEl.value
    console.log(userName, pass)
    connectSocket.send(JSON.stringify({
        action: "8",
        userName,
        pass
    }))
}
