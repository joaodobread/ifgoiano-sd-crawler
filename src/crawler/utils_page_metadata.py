class UtilsPageMetadata:
    MAIN_TEXT_ID = 'mw-content-text'

    INDEX_TOC_ID = 'toc'

    TOCCOLOURS_CLASS = 'toccolours'
    INFO_BOX_CLASS = 'infobox infobox_v2'
    THUMB_TRIGHT_CLASS = 'thumb tright'
    THUMB_TLEFT_CLASS = 'thumb tleft'
    NAV_BOX_CLASS = 'thumb tleft'
    NO_PRINT_CLASS = 'noprint'
    PRINTABLE_FOOTER_CLASS = 'printfooter'
    MW_EDIT_SELECTION_CLASS = 'mw-editsection'
    MW_HEADLINE_CLASS = 'mw-headline'
    REFERENCE_LINK_CLASS = 'reference'
    NO_WRAP_LINKS_CLASS = 'nowraplinks'
    NAV_BOX_TITLE_CLASS = 'navbox-title'
    REF_LIST_CLASS = 'reflist'
    AUTHORITY_CONTROL_CLASS = 'nowraplinks hlist navbox-inner'
    CITATION_EXTERNAL_CLASS = 'citation web'
    EXTERNAL_TEXT_CLASS = 'external text'

    NO_SCRIPT_TAG = 'noscript'
    SCRIPT_TAG = 'script'

    TABLE_PRESENTATION_ROLE = 'presentation'

    REMOVABLES_TAGS = [
        NO_SCRIPT_TAG,
        SCRIPT_TAG,
    ]

    REMOVABLES_ROLES = [
        TABLE_PRESENTATION_ROLE,
    ]

    REMOVABLES_CLASSES = [
        INFO_BOX_CLASS,
        THUMB_TRIGHT_CLASS,
        THUMB_TLEFT_CLASS,
        NO_PRINT_CLASS,
        PRINTABLE_FOOTER_CLASS,
        NAV_BOX_CLASS,
        TOCCOLOURS_CLASS,
        MW_EDIT_SELECTION_CLASS,
        MW_HEADLINE_CLASS,
        REFERENCE_LINK_CLASS,
        NAV_BOX_TITLE_CLASS,
        REF_LIST_CLASS,
        AUTHORITY_CONTROL_CLASS,
        CITATION_EXTERNAL_CLASS,
        EXTERNAL_TEXT_CLASS
    ]

    REMOVABLES_IDS = [
        INDEX_TOC_ID,
    ]
