function a() {
  alert("13");
}
function b(a, b){
    c=parseInt(a);
    d=parseInt(b);
    console.log(d);
    return c;
}
function d() {
  alert("37");
}
function c(a){
  alert(a+1);
}
a();
d();
c(b());
aa = ['1']
bb = ['2']//you
ii = ['3']//me
yy = ['4']
zz = ['5']
cc = ['6']
pp = ['7']//heaven
xx = ['8']//mate
oo = ['9']//rhyme
tt = ['a']
qq = ['b']
gg = ['c']
wp = ['d']
ee = ['e']
ez = ['f']
zzz = ['4', '2', '8', '3', '1', '2', '9', '3', 'b', 'a', 'f', '5', 'c', '2', '8', '2', 'd', '5', 'f', '2', 'd', '2', '9', '2', 'f', 'a', 'f', '7', 'd'];
xxx = zz.concat(ii.concat(zz.concat(yy.concat(yy.concat(wp.concat(yy.concat(ii.concat(zz.concat(yy.concat(yy.concat(cc.concat(pp.concat(qq.concat(yy.concat(tt.concat(zz.concat(ii)))))))))))))))));
yyy = ['2', 'd', '6', 'a', '7', '3', '5', 'f', '4', 'a', '5', '3', '2', 'd', '6', '1', '6', 'c', '6', '5', '7', '2'];
yyy = yyy.concat('7');
gg = xxx;
wp = yyy;
ez = zzz;
myList = gg.concat(wp.concat(ez));
at = '';
ay = "";
var z;
var x;
var i;
for (i = 0; i < myList.length; i++) {
  x=i;
  alert(myList[i]);
  at += myList[i];
}
function flagEgidenYOL(hex) {//Delan Azabani
    //var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}
function printFlag(ay){
  var z = ay;
  flag = flagEgidenYOL(z);
}
printFlag();
