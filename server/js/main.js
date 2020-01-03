function sendFiles() {
    const xhr = new XMLHttpRequest(),
    method = "GET",
    url = "/cgi-bin/send.py"

xhr.open(method, url, true)
xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        const node = document.getElementById("container")
        const files = JSON.parse(this.responseText)
        files.files.forEach((item, index) => {
            node.innerHTML += `<p><a href='./send/${item}'>${item}</a><p>`
        })
    }
}
xhr.send()
}

sendFiles()