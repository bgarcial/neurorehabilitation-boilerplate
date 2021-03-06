from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.


class Field(models.Model):

    FIELD_TYPE_NATURE = 'Grama natural'
    FIELD_TYPE_ARTIFICIAL = 'Grama sintetica'

    FIELD_TYPE_CHOICES = (
        (FIELD_TYPE_NATURE, u'Grama natural'),
        (FIELD_TYPE_ARTIFICIAL, u'Grama sintetica'),
    )

    MODALITY_11 = 'Fútbol 11'
    MODALITY_8 = 'Fútbol 8'
    MODALITY_7 = 'Fútbol 7'
    MODALITY_6 = 'Fútbol 6'
    MODALITY_5 = 'Fútbol 5'
    # FUTSAL_MODALITY = 'Fútbol de salón'

    MODALITY_CHOICES = (
        (MODALITY_11, u'Fútbol 11'),
        (MODALITY_8, u'Fútbol 8'),
        (MODALITY_7, u'Fútbol 7'),
        (MODALITY_6, u'Fútbol 6'),
        (MODALITY_5, u'Fútbol 5'),
    )

    name = models.CharField(
        max_length=150,
        primary_key=True,
    )

    field_type = models.CharField(
        choices=FIELD_TYPE_CHOICES,
        default=False,
        blank=False,
        max_length=20,
        verbose_name=('Tipo de material/grama de la cancha')
    )

    modality = models.CharField(
        # choices=MODALITY_CHOICES,
        max_length=40,
        # default=True,
        blank=False,
        verbose_name='Modalidad'
    )

    photo = models.ImageField(upload_to='fields', blank=True, null=True)

    location = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.name, self.field_type, self.location)
        #return '%s' % (self.name,)


class Team(models.Model):

    MODALITY_8 = 'Fútbol 8'
    MODALITY_6 = 'Fútbol 6'

    MODALITY_CHOICES = (

        (MODALITY_8, u'Fútbol 8'),
        (MODALITY_6, u'Fútbol 6'),
    )

    EMPTY_CATEGORY = ''
    ENTERPRISE_CATEGORY = 'Empresa'
    TOWN_CATEGORY = 'Barrio'
    UNIVERSITY_CATEGORY = 'Universidad'
    SCHOOL_CATEGORY = 'Colegio'
    CHILDREN_CATEGORY = 'Infantil'
    MASTER_CATEGORY = 'Master'
    WITHOUT_CATEGORY = 'Sin Categoría'

    CATEGORY_CHOICES = (

        (EMPTY_CATEGORY, u''),
        (ENTERPRISE_CATEGORY, u'Empresa'),
        (TOWN_CATEGORY, u'Barrio'),
        (UNIVERSITY_CATEGORY, u'Universidad'),
        (SCHOOL_CATEGORY, u'Colegio'),
        (CHILDREN_CATEGORY, u'Infantil'),
        (MASTER_CATEGORY, u'Master'),
        (WITHOUT_CATEGORY, u'Sin Categoría'),
    )

    BRANCH_CHOICES = (
        ('', ""),
        ('Masculino', "Masculino"),
        ('Femenino', "Femenino"),
    )

    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    '''
    name = models.CharField(
        max_length=100,
        primary_key=True,
        # primary_key=True implies null=False and unique=True.
        # unique=True implies db_index
        # Only one primary key is allowed on an object
    )
    '''
    name = models.CharField(
        _('name'),
        max_length=30,
        primary_key=True,
        # unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            RegexValidator(
                # r'^[\w.ñ@+-]+$',
                r'^[\d\/. ()\-+ ]+$',
                _('Enter a valid name team. This value may contain only '
                  'letters, numbers ' 'and ./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A team with that name already exists."),
        },
    )

    image = models.ImageField(
        upload_to='fields',
        blank=True,
        null=True,
        verbose_name='Imagen de la plantilla o escudo'
    )

    '''
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='players',
        blank=True,
    )
    '''
    modality = models.CharField(
        choices=MODALITY_CHOICES,
        max_length=40,
        #default=True,
        blank=True,
        verbose_name='Modalidad'
    )

    branch = models.CharField(
        choices = BRANCH_CHOICES,
        max_length=12,
        default=False,
        blank=True,
        verbose_name='Rama'
    )

    # listohome_field = models.ManyToManyField(Field)
    # place_origin = models.CharField(max_length=150, blank=True, verbose_name='Lugar de origen')

    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=40,
        default = 'Sin Categoría',
        blank=True,
        verbose_name='Categoría'
    )

    category_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Nombre'
    )

    place_origin = models.ForeignKey(
        'games_information.Field',
        verbose_name='Lugar de origen',
        blank=True,
        null=True,
    )
    # players = Hacer un query de los jugadores
    game_day = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Reservas o frecuencia de juego'
    )

    def __str__(self):
        return '%s' % (self.name)

    '''
    def save(self, *args, **kwargs):
        self.full_clean() # performs regular validation then clean()
        super(Team, self).save(*args, **kwargs)

    def clean(self):
        """
        Custom validation (read docs)
        """
        if self.name:
            self.name = self.name.strip()
            http://stackoverflow.com/questions/5043012/django-trim-whitespaces-from-charfield
    '''

class Match(models.Model):

    ACCEPTED_CHALLENGE = 'Aceptado'
    PENDING_CHALLENGE = 'Pendiente'
    CANCELLED_CHALLENGE = 'Cancelado'
    FICHAJE = 'Fichaje'

    STATUS_CHALLENGE_CHOICES = (

        (ACCEPTED_CHALLENGE, u'Aceptado'),
        (PENDING_CHALLENGE, u'Pendiente'),
        (CANCELLED_CHALLENGE, u'Cancelado'),
        (FICHAJE, u'Fichaje'),
    )

    home_team = models.ForeignKey(
        'games_information.Team',
        null=False,
        blank=True,
        verbose_name='Equipo local',
        related_name='hometeam'
    )

    away_team = models.ForeignKey(
        'games_information.Team',
        null=False,
        blank=True,
        verbose_name='Equipo visitante',
        #related_name=''
    )

    check_match_away_team = models.BooleanField(default=False)

    field = models.ForeignKey(
        'games_information.Field',
        null=False,
        blank=True,
        verbose_name='Lugar'

    )

    match_date = models.DateTimeField(default=timezone.now, null=False)

    status_challenge = models.CharField(
        choices=STATUS_CHALLENGE_CHOICES,
        max_length=40,
        verbose_name='Estado del desafío'
    )

    '''
    match_status = models.CharField(

    )
    '''

    home_team_players_accept = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='home_team_players_accept',
        blank=True,)

    away_team_players_accept = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='away_team_players_accept',
        blank=True,)

    home_team_players_cancel = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='home_team_players_cancel',
        blank=True,)

    away_team_players_cancel = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='away_team_players_cancel',
        blank=True,)

    fichaje_players_match = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='fichaje_players_match',
        blank=True,)

    def __str__(self):
        return "{} {} {} {}".format('Cotejo - ', self.home_team, 'vs.', self.away_team)
        # return '%s' % (self.name)


