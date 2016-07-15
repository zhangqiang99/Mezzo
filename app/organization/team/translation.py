from modeltranslation.translator import translator, register, TranslationOptions

from organization.team.models import *


@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):

    fields = ('description',)


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):

    fields = ('name', 'description',)


@register(Team)
class TeamTranslationOptions(TranslationOptions):

    fields = ('name', 'description',)


@register(Person)
class PersonTranslationOptions(TranslationOptions):

    fields = ('bio',)


@register(Activity)
class ActivityTranslationOptions(TranslationOptions):

    fields = ('description', 'content')