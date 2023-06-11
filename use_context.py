#https://youtu.be/L3T4D_YZwKA

from fastapi import FastAPI
from reactpy import component, use_state, use_context,create_context, html
from reactpy.backend.fastapi import configure



my_context = create_context(None)

@component
def root_path():
    #Now create context
    name,set_name = use_state("VK Context Test")
    return my_context(myparent(), value=[name,set_name])


@component
def myparent():

    return html.div(
        {
            "style": {
                 "background_color" : "orange",
                 "color": "white", "padding": "10px"
            }
        },
        html.h1("This is Parent component"),
        child()
    )


@component
def child():

    name,set_name = use_context(my_context)

    return html.div(
        {
            "style": {
                 "background_color" : "yellow",
                 "color": "blue", "padding": "10px"
            }
        },
        html.h1("This is child component"),
        html.h1(name),
        html.input({
            "type": "text",
            "on_change":lambda event:set_name(event['target']['value'])
        })
    )



app = FastAPI()
configure(app,root_path)