$(document).ready(function (){
    const map = new Datamap({
        element: document.getElementById('container'),
        fills: {
            WITH_SURVEY_DATA: '#008B8B',
            defaultFill: '#DC143C'
        },
        data: {
            // all other country code is at: https://gist.github.com/rendon/fc9d5b02a724979e878e
            CHN: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            USA: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            GBR: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            CAN: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            ROU: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            CHE: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            RWA: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            FRA: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            CYP: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            ISR: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            PRT: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            IRL: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            DEU: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            AUS: {
                fillKey: 'WITH_SURVEY_DATA'
            },
            NZL: {
                fillKey: 'WITH_SURVEY_DATA'
            }
        },
        done: function (datamap) {
            datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
                console.log(geography.properties.name);
                const tmp_url = "/api/query_survey_results/" + geography.properties.name;
                $.get(tmp_url, function(data, status) {
                    if (status == 'success') {
                        $("#container").hide();
                        console.log(status);
                        //$("#result_p").text(JSON.parse(data)['group 3'].query_results);
                        const w = 3500;
                        const h = 3000;

                        let dataset = {
                            nodes: [],
                            edges: []
                        };

                        for (let j = 1; j <= 4; j++) {
                            let group_desc = JSON.parse(data)[`group ${j}`].group_desc;
                            let group_data = JSON.parse(data)[`group ${j}`].query_results;
                            console.log(group_data);

                            if (Array.isArray(group_data[1])) {
                                for (let k = 0; k < group_data.length; k++) {
                                    dataset.nodes.push({
                                        name: `Group ${j} (${k})`,
                                        description: [-k, group_desc],
                                        color_original: '#DC143C',
                                        color_hover: '#008B8B'
                                    });
                                    let ruleIndex = dataset.nodes.length - 1;

                                    for (let i = 0; i < group_data[k].length; i++) {
                                        dataset.nodes.push({
                                            name: `User ${i}`,
                                            description: [k, group_data[k][i]],
                                            color_original: '#FF7F50',
                                            color_hover: '#9932CC'
                                        });
                                        dataset.edges.push({
                                            source: ruleIndex,
                                            target: dataset.nodes.length - 1
                                        })
                                    }
                                }
                            } else {
                                dataset.nodes.push({
                                    name: `Group ${j}`,
                                    description: [-j, group_desc],
                                    color_original: '#DC143C',
                                    color_hover: '#008B8B'
                                });
                                let ruleIndex = dataset.nodes.length - 1;

                                for (let i = 0; i < group_data.length; i++) {
                                    dataset.nodes.push({
                                        name: `User ${i}`,
                                        description: [j, group_data[i]],
                                        color_original: '#FF7F50',
                                        color_hover: '#9932CC'
                                    });
                                    dataset.edges.push({
                                        source: ruleIndex,
                                        target: dataset.nodes.length - 1
                                    })
                                }
                            }
                        }

                        // Constructs a new force-directed layout, used for graph a lot
                        var force = d3.layout.force()
                            // the nodes of a graph
                            .nodes(dataset.nodes)
                            // the edges of a graph
                            .links(dataset.edges)
                            // the size of the graph
                            .size([w, h])
                            .linkDistance([200])
                            // the strength of the force
                            .charge([-1200])
                            // start the force
                            // The force layout runs asynchronously. That is, when you call force.start()
                            .start();


                        // create a svg element
                        var svg = d3.select("body")
                            .append("svg")
                            .attr("width", w)
                            .attr("height", h);

                        // dynamically create graph edges
                        var edges = svg.selectAll("line")
                            .data(dataset.edges)
                            // .enter() creates the initial join of data to elements
                            // this can be very complex, please use it here for now
                            // later we may introduce these type of functions
                            .enter()
                            .append("line")
                            // line color
                            .style("stroke", "#ccc")
                            // line width
                            .style("stroke-width", 1);

                        // dynamically create graph nodes
                        var nodes = svg.selectAll("circle")
                            .data(dataset.nodes)
                            .enter()
                            // circle shape
                            .append("circle")
                            // radius is 10
                            .attr("r", 10)
                            // fill colors
                            // different from our previous example
                            .style("fill", function (d, i) {

                                return dataset.nodes[i].color_original;

                            })
                            // allow users to drag nodes
                            .call(force.drag);


                        // different from our previous example
                        // we define mouseover and mouse out event
                        nodes
                            .on('mouseover', function (d) {
                                // Highlight the nodes
                                // nodes.style('fill', d.color_original)
                                d3.select(this).style('fill', d.color_hover)
                            })
                            .on('mouseout', function (d) {
                                d3.select(this).style('fill', d.color_original)
                            })
                            .on('click', function (d, i) {
                                console.log('you click on the node:' + d.name + '; Here is the user story: ' + d.description[1]);
                                if(d.name.includes("Group")){
                                    window.alert(d.description[1]);
                                }
                                else{
                                    $('#exampleModalLongTitle').text(d.description[1][0] + ' ');
                                    $('#modal_country').text(d.description[1][1]);
                                    $('#modal_age').text(d.description[1][2]);
                                    $('#modal_gender').text(d.description[1][3]);
                                    $('#modal_fear').text(d.description[1][4]);
                                    $('#modal_anxious').text(d.description[1][5]);
                                    $('#modal_angry').text(d.description[1][6]);
                                    $('#modal_happy').text(d.description[1][7]);
                                    $('#modal_sad').text(d.description[1][8]);
                                    $('#modal_emotion').text(d.description[1][9]);
                                    $('#modal_explain').text(d.description[1][10]);
                                    $('#modal_meaning').text(d.description[1][11]);
                                    $('#modal_occupation').text(d.description[1][12]);
                                    $('#itemModal').modal('show');
                                }
                            });

                        // different from our previous example
                        // dynamically create labels
                        var label = svg.selectAll(".mytext")
                            .data(dataset.nodes)
                            .enter()
                            .append("text")
                            .text(function (d) {
                                return d.name;
                            })
                            // where we want to render the label, start | middle | end
                            .style("text-anchor", "middle")
                            // color
                            .style("fill", "#555")
                            .style("font-family", "Arial")
                            .style("font-size", 12);


                        // read this: https://stackoverflow.com/questions/28745398/why-do-we-need-force-ontick-in-d3
                        // The tick handler is the function that enables you to get the state of the layout when it has changed
                        // (the simulation has advanced by a tick) and act on it -- in particular,
                        // redraw the nodes and links where they currently are in the simulation.
                        force.on("tick", function () {
                            edges.attr("x1", function (d) {
                                return d.source.x;
                            })
                                .attr("y1", function (d) {
                                    return d.source.y;
                                })
                                .attr("x2", function (d) {
                                    return d.target.x;
                                })
                                .attr("y2", function (d) {
                                    return d.target.y;
                                });
                            nodes.attr("cx", function (d) {
                                return d.x;
                            })
                                .attr("cy", function (d) {
                                    return d.y;
                                });
                            label.attr("x", function (d) {
                                return d.x;
                            })
                                .attr("y", function (d) {
                                    return d.y - 10;
                                });

                        });
                    }
                });
            });
        }
    });
    // Draw a legend for this map
    map.legend();
})