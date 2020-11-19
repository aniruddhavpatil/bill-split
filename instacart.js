var array = $("div.item-delivered");

var items = '\n'
$.each(array, (i, v) => {
    var curr_name = v.children[1].innerHTML.split('\n')[1].replace(/ /g, '_');
    var curr_price = v.children[2].children[0].children[0].innerHTML.replace('$', '');
    items += curr_name + '\t' + curr_price + '\n';
})

console.log(items);