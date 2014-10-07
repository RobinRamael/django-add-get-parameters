# django-add-get-param

This small app contains a template tag to add a get parameter to the current url.

## Usage:

Suppose the following template is loaded at the url http://example.com/search?q=searchquery :


    {% load add_get_parameter %}

    ...

    {% add_get param1='const' param2=variable_in_context %}


The add_get tag will now output the url `http://example.com/search?q=searchquery&param1=const&param2={{variable_in_context}}`. That's pretty much it.

## Attribution

This app is based on the [django snippet written by user naktinis](https://djangosnippets.org/snippets/2428/). The standalone app was put together by Robin Ramael.

## License

This project is released under the Apache License 2.0
