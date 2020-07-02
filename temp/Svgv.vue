Vue.component('Svgv', {
  props:[ 'data'],
  data:function(){
    return {
		attrs:{width:"500", height:"250", version:"1.1", xmlns:"http://www.w3.org/2000/svg"},
		childrens:[
			{
				element:'rect', 
				attrs:
				{
					'x':'10', 'y':'10', 'width':'70', 'height':'70', 'stroke':'black', 'fill':'transparent', 'stroke-width':'5'
				},
			},
			{
				element:'rect', 
				attrs:
				{
					'x':'70', 'y':'70', 'width':'30', 'height':'30', 'stroke':'black', 'fill':'transparent', 'stroke-width':'5'
				},
			},
		]
    }
  },
  methods:{
  },
  created() {
    
  },
  render: function (createElement) {
	var self = this;	
	function recEl(j){
		var e = [];
		for(var i in j){
			e.push(createElement(Vue.options.components['SvgvElement'], {attrs:{data:j[i], childrens:j[i].childrens}}, childrens));
		}
		return e;
	}	
	var childrens = recEl(this.childrens);
	return createElement('svg', {attrs:this.attrs},childrens)  
  },
})
