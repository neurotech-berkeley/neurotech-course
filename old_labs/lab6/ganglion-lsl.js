// code by Alexandre Barachant

const Ganglion = require('openbci-ganglion').Ganglion;
const ganglion = new Ganglion();
// Construct LSL Handoff Python Shell
var PythonShell = require('python-shell');
var lsloutlet = new PythonShell('LSLHandoff.py');

lsloutlet.on('message', function(message){
    console.log('LslOutlet: ' + message);
});
console.log('Python Shell Created for LSLHandoff');

ganglion.once('ganglionFound', (peripheral) => {
  // Stop searching for BLE devices once a ganglion is found.
  ganglion.searchStop();
  ganglion.on('sample', (sample) => {
    /** Work with sample */
    st = sample.channelData.join(' ');
    var s = ''+ sample.timeStamp + ': '+ st
    lsloutlet.send(s)
  });
  ganglion.once('ready', () => {
    ganglion.streamStart();
  });
  ganglion.connect(peripheral);
});
// Start scanning for BLE devices
ganglion.searchStart();
