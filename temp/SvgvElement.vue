Vue.component('SvgvElement', {
  props:[ 'data', 'childrens'],
  data:function(){
    return {
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
	return createElement(this.data.element, {attrs:this.data.attrs},childrens)  
}
})
