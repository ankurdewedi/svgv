Vue.component('Svgv', {
  props:[ 'data'],
  data:function(){
    return {
		attrs:this.data.attrs,
		childrens:this.data.childrens
    }
  },
  methods:{
  },
  beforeMount(){
    
  },
  created() {
    
  },
  render: function (createElement) {
	var self = this;	
	function recEl(j){
		var e = [];
		for(var i in j){
			e.push(
				createElement(
					Vue.options.components['SvgvElement'], 
					{
						attrs:
						{
							data:j[i], 
							childrens:j[i].childrens
						},
						on:{
							click:function(e){
								self.$emit('click', event);
							},
						}
					}, 
					childrens
				)
			);
		}
		return e;
	}	
	var childrens = recEl(this.childrens);
	return createElement(
			'svg', 
			{
				attrs:this.attrs,
				on:{
					click:function(e){
						self.$emit('clicksvg', event);
					},
				},
			},
			childrens
		)  
  },
})
