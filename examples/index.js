new Vue({
  el: '#app',
  data: function () {
	return {
		data:{
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
	}
  },
  methods:{
	
  },
  template: `<svgv :data="data"></svgv>`
})
