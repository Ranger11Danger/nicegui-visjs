export default {
  template: "<div></div>",
  props: {
    initialData: {
      type: Object,
      default: () => ({ nodes: [], edges: [] })
    },
  },
  mounted() {
    var nodes = new vis.DataSet(this.initialData.nodes);
    var edges = new vis.DataSet(this.initialData.edges);

    var data = {
      nodes: nodes,
      edges: edges
    };

    var options = {
      nodes: {
        shape: 'dot',
        size: 30,
        font: {
          size: 32,
          color: '#ebebeb'
        },
        borderWidth: 2
      },
      edges: {
        width: 2
      }
    };

    this.network = new vis.Network(this.$el, data, options);
  },
   methods: {
    add_node(node) {
      this.network.body.data.nodes.add(node);
    },
    delete_node(id) {
      this.network.body.data.nodes.remove(id);
    },
    add_edge(edge) {
      this.network.body.data.edges.add(edge);
    },
    delete_edge(id) {
      this.network.body.data.edges.remove(id);
    },
  },
  beforeDestroy() {
    if (this.network) {
      this.network.destroy();
    }
  },
};

