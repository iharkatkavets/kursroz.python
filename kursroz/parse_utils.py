from xml.etree import ElementTree
from xml.parsers.expat import ExpatError
from .item_metadata import ItemMetadata
from .date_parsers import parse_date

def parse_items(xml):
    try:
        root = ElementTree.fromstring(xml)
    except ExpatError as e:
        print(f'[XML] Error (line {e.lineno}): {e.code}')
        print(f'[XML] Offset: {e.offset}')
        raise e
    except IOError as e:
        print(f'[XML] I/O Error {e.errno}: {e.strerror}')
        raise e
    else:
        list = []
        for item in root.iter('item'):
            title_element = item.find('title')
            assert title_element is not None
            pub_date_element = item.find('pubDate')
            assert pub_date_element is not None
            link_element = item.find('link')
            assert link_element is not None
            enclosure_element = item.find('enclosure')
            assert enclosure_element is not None
            metadata = ItemMetadata(title_element.text,
                                    parse_date(pub_date_element.text),
                                    enclosure_element.get('url'),
                                    link_element.text)
            list.append(metadata)
        return list

def parse_usd_rate(xml):
    try:
        root = ElementTree.fromstring(xml)
    except ExpatError as e:
        print(f'[XML] Error (line {e.lineno}): {e.code}')
        print(f'[XML] Offset: {e.offset}')
        raise e
    except IOError as e:
        print(f'[XML] I/O Error {e.errno}: {e.strerror}')
        raise e
    else:
        for item in root.iter('pozycja'):
            currency_code_element = item.find('kod_waluty')
            assert currency_code_element is not None
            if currency_code_element.text == 'USD':
                rate_element = item.find('kurs_sredni')
                if rate_element is not None and rate_element.text is not None:
                    return rate_element.text
                else:
                    raise RuntimeError("")
        return None
