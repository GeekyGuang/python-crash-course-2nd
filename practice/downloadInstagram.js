// 获取下载链接
const items = document.querySelectorAll('.download')
const itemsArray = [...items]
const itemshref = itemsArray.map(item => item.href).join('\n')


// 自定义从控制台将变量保存到本地的函数
;(function(console) {
  console.save = function(data, filename) {
    if (!data) {
      console.error("Console.save: No data")

      return
    }

    if (!filename) filename = "console.json"

    if (typeof data === "object") {
      data = JSON.stringify(data, undefined, 4)
    }

    var blob = new Blob([data], { type: "text/json" }),
      e = document.createEvent("MouseEvents"),
      a = document.createElement("a")

    a.download = filename

    a.href = window.URL.createObjectURL(blob)

    a.dataset.downloadurl = ["text/json", a.download, a.href].join(":")

    e.initMouseEvent("click",true,false,window,0,0,0,0,0,false,false,false,false,0,null,)

    a.dispatchEvent(e)
  }
})(console)

// 保存到本地
console.save(itemshref, '下载链接.txt')