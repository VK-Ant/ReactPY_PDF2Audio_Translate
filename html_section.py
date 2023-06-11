from reactpy import html, component, run
'''
html.div(
    html.h1("My favorite fighters"),
    html.ul(
        html.li("Ali"),
        html.li("lee"),
        html.li("white"),
    )
)
'''

@component
def Photo():


    return html.img(
        {
            "src": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.1ydLMwUjEboJ_ZPS0IzMzwHaE8%26pid%3DApi&f=1&ipt=69a48e9c9b4c577679e76d560133a109c77dc83149804c8ea719174879a7bb89&ipo=images",
            "style": {"width":"50%"},
            "alt": "Cutty"
        }
    )

run(Photo)