function key(url){
    var curUrl = url;
    var sig = "";
    var chars = "0123456789abcdef";
    var curTime = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "" + Date.parse(new Date());
    sig = chars.charAt(parseInt(Math.random() * (15 - 15 + 1) + 10)) + chars.charAt(curTime.length) + "" + curTime;

    var key = "";
    var keyIndex = -1;

    for (var j = 0; j < 6; j++) {
    var d = sig.charAt(keyIndex + 1);
    key += d;
    keyIndex = chars.indexOf(d);
    if (keyIndex < 0 || keyIndex >= sig.length) {
        keyIndex = j;
        }
    }

    var timestamp = parseInt(Math.random() * (9999 - 1000 + 1) + 1000) + "_" + key + "_" + Date.parse(new Date());
    var t = timestamp;
    t = t.replace(/\+/g, "_");

    var tkey = "";
    var tkeyIndex = -1;
    for(var i=0;i<6;i++){
        var c=timestamp.charAt(tkeyIndex+1);
        tkey +=c;
        tkeyIndex = chars.indexOf(c);
        if(tkeyIndex<0 || tkeyIndex>=timestamp.length){
            tkeyIndex = i;
        }
    }

    curUrl += "?s=" + sig;
    curUrl += "&t=" + t;
    curUrl += "&o=" + tkey;

    return curUrl
}

