/**
 *   Visualizations in the Municipaliy dashboard
 */

d3.json('/api/test', function(data){
    for(var i = 0; i < data.length; i++) {
        console.log(data[i]);
    }
});
