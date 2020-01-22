<! DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>javascript for loop</ title>
</ head>
<body>
<script>
    // output loop
    function xh() {
       var r="";
       var o="";
        for(var w=0;w<10;w++){
           r+="hey i love you:"+w+"<br>";
           document.getElementById("demo").innerHTML=r;
       }
       // loop list
        listw = ["Jinmu","Sasaki Gosei","Small White Hair Kinmu","Black Hair Kinmu","340","Black Death"];
       for(k=0;k<listw.length;k++){
            document.getElementById("demo2").style.color="green";
            document.getElementById("demo2").innerHTML=o+="My name is:"+listw[k]+"<br>";
        }
    }
</script>
<p id="demo"></p>
<b id="demo2">Boschko</b>
<button onclick="xh()">Click</button>
</body>
</html>

// Due to the special nature of javascript, I want to output a loop on the html much more. Define an empty variable and then add it up.
