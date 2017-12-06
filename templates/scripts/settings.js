var ConfigurationService = function(){
    return {
        data: {},

        getData: function(){
            return this.data;
        },

        setData: function(data){
            this.data = data;
        },

        /**
         *  Sorts data into a hierarchical tree and returns it
         */
        getTree : function()
        {
            /// Get fields
            var total = {};
            var exceptions = [ 'year' ];
            for(field in this.data[0])
                if(exceptions.indexOf(field) == -1)
                    total[field] = this.data[0][field];
            for(var i = 1; i < this.data.length; i++)
                for(field in total)
                    total[field] += this.data[i][field];
            var graph = {
                name     : "Budget allocation " + this.data[0].year + "-" + this.data[this.data.length-1].year,
                children : [],
            };
            for(var category in this.first_level_categories){
                var first_level_child = {
                    'name'     : this.first_level_categories[category].v,
                    'children' : [],
                };
                // TODO -> ES 5
                var leafs = Object.keys(total).filter(
                    label => label.indexOf("concept_" + this.first_level_categories[category].k) > -1
                );
                for(i in leafs){
                    first_level_child.children.push({
                        'name'  : leafs[i],
                        'value' : total[leafs[i]],
                    });
                };
                graph.children.push( first_level_child );
            };
            return d3.hierarchy(graph)
                     .eachBefore(function(d) { d.data.id = (d.parent ? d.parent.data.id + "." : "") + d.data.name; })
                     .sum(function(d) { return d.value; })
                     .sort(function(a, b) { return b.height - a.height || b.value - a.value; });
        },


        /**
         *  Time series
         */
        getTimeseries : function(concept){
            var timeseries = [];
            for(var i in this.data){
                timeseries.push( this.data[i][concept] );
            }
            return timeseries;
        },

        getSparkline : function(category, w, h){
            var padding = 20;
            var points = "";
            var timeline_data = this.getTimeseries(category);
            var y_scale = d3.scaleLinear().domain([2e6, 20e6]).range([h*.75, h*.25]);
            var slot = w*.8 / timeline_data.length+1;
            for(var i in timeline_data){
                var x = w*.1 + slot*i;
                var y = d3.format("d")(y_scale(timeline_data[i]));
                points += [x, y].join(",") + " ";
            }
            return points;
        },

        first_level_categories : [
          { k: 'ps', v : 'General public services' },
          { k: 'de', v : 'Defence' },
          { k: 'po', v : 'Public order and safety' },
          { k: 'ea', v : 'Economic affairs' },
          { k: 'ep', v : 'Environmental protection' },
          { k: 'ho', v : 'Housing and community amenities' },
          { k: 'he', v : 'Health'  },
          { k: 're', v : 'Recreation, culture and religion' },
          { k: 'ed', v : 'Education'  },
          { k: 'so', v : 'Social protection' },
        ],

        first_level_colors : [
          '#ed4040',
          '#eda640',
          '#ceed40',
          '#69ed40',
          '#40ed7d',
          '#40ede3',
          '#4091ed',
          '#5440ed',
          '#ba40ed',
          '#ed40ba'
        ],

        color : function(index){
           return this.first_level_colors[index];
        },

        subcolor : function(index){
           return d3.interpolateRgb(
              this.first_level_colors[index], "#fff"
           )(.2 + Math.random()*.1)
        },

        second_level_categories : {
          'concept_ps_1' : ['Executive and','legislative organs','financial and','fiscal affairs,', 'external affairs'],
          'concept_ps_2' : ['Foreign','economic aid'],
          'concept_ps_3' : ['General','services'],
          'concept_ps_4' : ['Basic','research'],
          'concept_ps_5' : ['R&D general','public services'],
          'concept_ps_6' : ['General public','services','(not classified)'],
          'concept_ps_7' : ['Public debt','transactions'],
          'concept_ps_8' : ['Transfers of a general','character between','different levels','of government'],
          'concept_de_1' : ['Military defence'],
          'concept_de_2' : ['Civil defence'],
          'concept_de_3' : ['Foreign military aid'],
          'concept_de_4' : ['R&D defence'],
          'concept_de_5' : ['Defence','(not classified)'],
          'concept_po_1' : ['Police','services'],
          'concept_po_2' : ['Fire-protection','services'],
          'concept_po_3' : ['Law courts'],
          'concept_po_4' : ['Prisons'],
          'concept_po_5' : ['R&D public order','and safety'],
          'concept_po_6' : ['Public order','and safety','(not classified)'],
          'concept_ea_1' : ['General economic,','commercial','and labour affairs'],
          'concept_ea_2' : ['Agriculture,','forestry,','fishing and hunting'],
          'concept_ea_3' : ['Fuel and energy'],
          'concept_ea_4' : ['Mining, manufacturing','and construction'],
          'concept_ea_5' : ['Transport'],
          'concept_ea_6' : ['Communication'],
          'concept_ea_7' : ['Other industries'],
          'concept_ea_8' : ['R&D economic','affairs'],
          'concept_ea_9' : ['Economic affairs','(not classified)'],
          'concept_ep_1' : ['Waste','management'],
          'concept_ep_2' : ['Waste','water management'],
          'concept_ep_3' : ['Pollution','abatement'],
          'concept_ep_4' : ['Protection of biodiversity','and landscape'],
          'concept_ep_5' : ['R&D environmental protection'],
          'concept_ep_6' : ['Environmental','protection','(not classified)'],
          'concept_ho_1' : ['Housing','development'],
          'concept_ho_2' : ['Community','development'],
          'concept_ho_3' : ['Water','supply'],
          'concept_ho_4' : ['Street','lighting'],
          'concept_ho_5' : ['R&D housing','and community','amenities'],
          'concept_ho_6' : ['Housing','and community','amenities','(not classified)'],
          'concept_he_1' : ['Medical products,','appliances and equipment'],
          'concept_he_2' : ['Outpatient','services'],
          'concept_he_3' : ['Hospital','services'],
          'concept_he_4' : ['Public health','services'],
          'concept_he_5' : ['R&D health'],
          'concept_he_6' : ['Health','(not classified)'],
          'concept_re_1' : ['Recreational','and sporting','services'],
          'concept_re_2' : ['Cultural','services'],
          'concept_re_3' : ['Broadcasting','and publishing','services'],
          'concept_re_4' : ['Religious and','other community services'],
          'concept_re_5' : ['R&D recreation,','culture and religion'],
          'concept_re_6' : ['Recreation,','culture','and religion (not classified)'],
          'concept_ed_1' : ['Pre-primary','and primary','education'],
          'concept_ed_2' : ['Secondary education'],
          'concept_ed_3' : ['Post-secondary','non-tertiary education'],
          'concept_ed_4' : ['Tertiary','education'],
          'concept_ed_5' : ['Education','not definable','by level'],
          'concept_ed_6' : ['Subsidiary','services','to education'],
          'concept_ed_7' : ['R&D','education'],
          'concept_ed_8' : ['Education','(not classified)'],
          'concept_so_1' : ['Sickness','and disability'],
          'concept_so_2' : ['Old age'],
          'concept_so_3' : ['Survivors'],
          'concept_so_4' : ['Family','and children'],
          'concept_so_5' : ['Unemployment'],
          'concept_so_6' : ['Housing'],
          'concept_so_7' : ['Social','exclusion','(not classified)'],
          'concept_so_8' : ['R&D social','protection'],
          'concept_so_9' : ['Social','protection','(not classified)'],
        },

        getSubcategoryLabel : function(k){
            return this.second_level_categories[k];
        },

        currency_locale : d3.formatLocale ({
            "decimal": ".",
            "thousands": " ",
            "currency": ["", " M. €"],
            "grouping": [3],
        }),

        currency : function(amount){
            return this.currency_locale.format("$d")(amount/1e6)
        },
    }
};
