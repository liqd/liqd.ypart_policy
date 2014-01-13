# -*- coding: utf-8 -*-
from liqd.ypart_theme.interfaces import IProjekteViewletMarker
from plone.dexterity.interfaces import IDexterityContent
from plone.api.content import create
from plone.app.layout.navigation.interfaces import INavigationRoot
from zope.interface import alsoProvides


def setupVarious(context):
    """set some initial content"""
    site = context.getSite()
    if context.readDataFile('liqd.ypart_policy.txt') is None:
        return
    #delete archetype content
    delete = ['Members', 'front-page', 'news', 'events']
    for del_ in delete:
        if site.hasObject(del_):
            if not IDexterityContent.providedBy(site[del_]):
                site.manage_delObjects(del_)
    # create dx content
    if not site.hasObject('de'):
        content = create(type='Folder', container=site,
                         id='de', title="DE Übersetzungen")
        content.reindexObject()
    if not site['de'].hasObject('youthpart'):
        content = create(type='Folder', container=site['de'],
                         id='youthpart', title='Youthpart')
        alsoProvides(content, INavigationRoot)
        content.reindexObject()
    if not site['de']['youthpart'].hasObject('front-page'):
        content = create(type='Document', container=site['de']['youthpart'],
                         id='front-page', title='Youthpart')

        alsoProvides(content, IProjekteViewletMarker)
        content.reindexObject()
    if not site['de']['youthpart'].hasObject('national'):
        content = create(type='Folder', container=site['de']['youthpart'],
                         id='national', title='National')
        content.reindexObject()
    if not site['de']['youthpart'].hasObject('lokal'):
        content = create(type='Folder', container=site['de']['youthpart'],
                         id='lokal', title='Lokal')
        content.reindexObject()
    if not site['de']['youthpart'].hasObject('blog'):
        content = create(type='Folder', container=site['de']['youthpart'],
                         id='blog', title='Blog')
        content.reindexObject()
    if not site['de'].hasObject('mainnav'):
        content = create(type='Folder', container=site['de'],
                         id='mainnav', title='Hauptnavigation')
        content.reindexObject()
    if not site['de']['mainnav'].hasObject('about_ypart.html'):
        content = create(type='Folder', container=site['de']['mainnav'],
                         id='about_ypart.html', title='Über Uns')
        content.reindexObject()
    if not site['de']['mainnav']['about_ypart.html'].hasObject('about'):
        content = create(type='Document',
                         container=site['de']['mainnav']['about_ypart.html'],
                         id='about', title='Über Uns',)
        content.reindexObject()
    if not site['de']['mainnav'].hasObject('donations.html'):
        content = create(type='Folder', container=site['de']['mainnav'],
                         id='donations.html',
                         title='Unterstützte uns')
        content.reindexObject()
    if not site['de']['mainnav']['donations.html'].hasObject('donations'):
        content = create(type='Document',
                         container=site['de']['mainnav']['donations.html'],
                         id='donations',
                         title='Unterstützte uns',)
        content.reindexObject()
    if not site['de']['mainnav'].hasObject('support.html'):
        content = create(type='Folder', container=site['de']['mainnav'],
                         id='support.html', title='Hilfe')
        content.reindexObject()
    if not site['de']['mainnav']['support.html'].hasObject('support'):
        content = create(type='Document',
                         container=site['de']['mainnav']['support.html'],
                         id='support', title='Hilfe',)
        content.reindexObject()
