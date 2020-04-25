const { app, BrowserWindow } = require('electron')

function createWindow () {
  // Create the browser window.
  // let win = new BrowserWindow({
    // width: 620,
    // height: 565,
    // webPreferences: {
    //   nodeIntegration: true
    // }
  // })

  let win = new BrowserWindow({frame: false, transparent: true})
  // win.webContents.openDevTools()
  // win.setMenu(null)
  // and load the index.html of the app.
  win.loadFile('index.html')
}

app.on('ready', createWindow)