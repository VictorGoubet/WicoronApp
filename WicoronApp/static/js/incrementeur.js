Panier=[];

function incInput(i,id) {
    sp=id.split('_');
    var newid='IDinpt_'+sp[1];
    var value =parseInt(document.getElementById(newid).value,10);
    if((value>0 || i==1)&& !(value==20 && i==1)){
        value += i;
        document.getElementById(newid).value = value;
    }
    
}
