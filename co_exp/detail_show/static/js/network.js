$(document).ready(function () {
    // $("#network").html("<img src='/static/img/loading.gif'/>");
    var parameter = $("#network").data("url");
    $.ajax({
        url: "/network?" + parameter,
        type: "get",
        dataType: "json",
        success: function (data) {
            var network;
            var nodesDataset = new vis.DataSet(data.nodes);
            var edgesDataset = new vis.DataSet(data.edges);

            var container = document.getElementById('network');
            var options = {
                autoResize: true,
                nodes: {
                    shape: 'dot',
                    size:5,
                    borderWidth:0,
                    borderWidthSelected:0,
                    font: '12px arial #333'
                },
                groups: {
                    geneGroup: {color:{background:'red'}, borderWidth:0,size:10}
                },
                physics:false,
                edges: {
                    width: 0.2,
                    color: '#999',
                    smooth: {
                        type: 'continuous'
                    }
                },
                interaction: {
                    hover: true,
                    hideEdgesOnDrag: true,
                    tooltipDelay: 50
                }
            };
            var data1 = {nodes: nodesDataset, edges: edgesDataset};


            network = new vis.Network(container, data1, options);

            //network.on("click",neighbourhoodHighlight);
        }

    });
})
;