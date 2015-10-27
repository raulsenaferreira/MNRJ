var express = require('express');
var multer = require('multer');
var app = express();
var http = require('http').Server(app);
var upload = multer({ dest: './uploads/'});
var PythonShell = require('python-shell');

app.use("/css", express.static(__dirname + '/css'));
app.use("/js", express.static(__dirname + '/js'));
app.use("/img", express.static(__dirname + '/img'));
app.use("/fonts", express.static(__dirname + '/fonts'));
app.use("/font-awesome/css/", express.static(__dirname + '/font-awesome/css/'));

app.use(multer({ dest: './uploads/',
    rename: function (fieldname, filename) {
        return filename+Date.now();
    },
    onFileUploadStart: function (file) {
        console.log('Subindo arquivo ' + file.originalname + ' ...');
    },
    onFileUploadComplete: function (file) {
        console.log(file.fieldname + ' salvo em ' + file.path)

        executePython(file.path);
    }
}));

app.get('/', function (req, res) {
  res.sendFile(__dirname +'/index.html');
});

app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if(err) {
            return res.end("Error uploading file.");
        }
        res.end("Upload de arquivo terminado com sucesso!");
    });
});

function executePython(filePath){
  var options = {
    mode: 'text',
    //pythonPath: 'path/to/python',
    //pythonOptions: ['-u'],
    //scriptPath: '/home/raul/MNRJ/',
    //args: ['value1', 'value2', 'value3']
    args: [filePath]
  };

  PythonShell.run('excel2dwca.py', options, function (err, results) {//excel2dwca
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    //console.log('results: %j', results);
    finalFile = options.args
    console.log('Arquivo disponivel em ' + __dirname + '/' + finalFile + '-CONVERTIDO.csv')
  });
}

http.listen(4000, function(){
  console.log('Disponível na porta 4000');
});
