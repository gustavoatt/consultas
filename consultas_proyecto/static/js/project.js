/* Project specific Javascript goes here. */
var search_bar_data_source = new Bloodhound({
  remote: "/pacientes/api/listar/?q=%QUERY",
  datumTokenizer: function(d) {
    return d;
  },
  queryTokenizer: Bloodhound.tokenizers.whitespace
});

search_bar_data_source.initialize();

$("#search_input").typeahead(null, {
  name: 'pacientes',
  displayKey: function(suggestion) {
    return suggestion['nombres'].split(" ")[0] + " " +
           suggestion['apellidos'].split(" ")[0];
  },
  source: search_bar_data_source.ttAdapter()
});
