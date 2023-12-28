'''
Notes for electron made ez by Oriel using python edition


1. Create a package.JSON file
1A. This is what it will look like

{
    "name": "cat_and_cake",
    "version": "1.0.0",
    "main": "main.js",
    "devDependencies": {
        "electron": "^28.1.0"
    },
    "scripts": {
        "start": "electron ."
    }
}


Main things to understand...
    - Always create a project name
    - Always create a project version
    - Always create a project main


The name, version, main are required to start the desktop app

    - main is where the electron app will open when the user clicks the .exe


    - Adding a scripts key with a value of 'electron .' will link the js file


2. Things to import

This is to test the client off jump - console.log('This bitch is running oh o ok')

const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');



3. Create a variable named 'win' and a function for the browser window

    - sample below to get started

    let win;

function createWindow() {
    win = new BrowserWindow();
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }));
    win.on('closed', () => {
        win = null;
    });
};

//Opens Dev tools in browser window when app is open
win.webContents.openDevTools();


app.on('ready', createWindow);

//This is for mac users
//If the platform is not equal to mac OS 'darwin' then close app (When clicking x to close)
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (win === null) {
        createWindow;
    }
});

'''


# Enjoy :)
