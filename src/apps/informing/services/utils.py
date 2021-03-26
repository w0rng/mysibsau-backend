from re import sub


def replace_vk_links_on_markdown(text: str) -> str:
    mask = r'(\[((id|club)\d+)\|([a-zA-Zа-яА-Я0-9 ]+)\])'
    repl = r'[\4](https://vk.com/\2)'

    return sub(mask, repl, text)
