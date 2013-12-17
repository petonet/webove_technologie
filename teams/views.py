# -*- coding: utf-8 -*-

from django.views import generic
from teams.models import Team, NewsFeeds, Gallery, UserInTeamNtoN
from players.models import player
from forms import addTeamForm,addRequestToTeam,deleteRequestToTeam
from django.shortcuts import render_to_response, RequestContext, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
import forms as formularis

class TeamsView(generic.ListView):
    model = Team
    template_name = 'teams\\teamslist.html'


class TeamsDetailView(generic.ListView):
    model = Team
    template_name = 'teams\\ground_detail.html'

def teamsListSorted(request,sortPar):
    if str(sortPar).startswith('name'):
        teams = Team.objects.all().order_by('name')
    if str(sortPar).startswith('counts_of_players'):
        teams = Team.objects.all().order_by('counts_of_players')
    if str(sortPar).startswith('reg_date'):
        teams = Team.objects.all().order_by('reg_date')
    if str(sortPar).startswith('counts_of_players'):
        teams = Team.objects.all().order_by('counts_of_players')
    if str(sortPar).endswith('Rev'):
        teams = teams.reverse()
    response = {
        'team_list' : teams,
    }
    return render_to_response('teams/teamslist.html',response, context_instance=RequestContext(request))

def findTeam(request):
    if request.method=="POST":
        if (len(request.POST['teamname'])) > 0:
            teams = Team.objects.all().filter(name__contains=request.POST['teamname'])
            if len(teams)==0:
                response = {
                    'fail' : 'Žiadny tím s takýmto názvom nebol nájdený !',
                }
            else:
                response = {
                    'team_list' : teams,
                }
        else:
                response = {
                    'fail' : 'Nič si nezadal !',
                }
    else:
        response = None
    return render_to_response('teams/findTeam.html',response, context_instance=RequestContext(request))
"""

class IndexView(generic.ListView):

    template_name = 'teams/index.html'
    context_object_name = 'teams_list'

    def get_queryset(self):
        return Team.objects.order_by('-reg_date')

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)

        for e in Team.objects.all():
            e.counts_of_players = UserInTeamNtoN(team_id=e.pk).objects.count()
            e.save()

        context['edited_team_list'] = Team.objects.order_by('-reg_date')

        return context


class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'

    def get_context_data(self, **kwargs):
        a = []
        PK = int(self.kwargs.get('pk', None))
        context = super(DetailView, self).get_context_data(**kwargs)
        #print 'toto je kontext id', self.kwargs.get('pk', None)
        #for e in UserInTeamNtoN.objects.filter(team_id=self.kwargs.get('pk', None)):
        #    a.append(player.objects.filter(pk=e.user_id.user_id)[0])
        #context['players'] = a


        try:
            selectedPLayer = self.request.user.get_profile()
        except player.DoesNotExist:
            selectedPLayer = player(user=self.request.user)

        member = UserInTeamNtoN.objects.filter(user_id=selectedPLayer)
        teamadmin = Team.objects.filter(leader=selectedPLayer)


        if len(teamadmin) > 0:
            if teamadmin[0].pk == PK :
                return redirect('/teams/myTeam/')

        if len(member) > 0:
            if teamadmin[0].pk == PK:
                if member[0].accepted==True :
                    return redirect('/teams/myTeam/')
                else:
                    context['playerRequest'] = True

        for e in UserInTeamNtoN.objects.filter(team_id=PK):
            a.append(player.objects.get(pk=e.user_id.pk))
        context['players'] = a

        #try:
        #    context['players'] = player(pk=UserInTeamNtoN(team_id=self.model.pk).user_id).objects.all()
        #except ValueError:
        #    print 'Error(Weak) - teams.views.DetailView - v danom time je len osoba ktora ho vytvorila'
        #    context['players'] = None

        #context['new_feeds'] = NewsFeeds(team_id=self.model.pk).objects.order_by('-publish_date')
        context['new_feeds'] = NewsFeeds.objects.filter(team_id=PK)
        context['GalleryTeam'] = Gallery.objects.filter(team_id=PK)
        #context['path'] = PROJECT_PATH.strip("\HrajAirsoft").replace('\\', '/') + "/"

        return context
"""
#Zrušenie poslanej ziadosti
@login_required
def cancelRequest(request):
    delInvitation = formularis.deleteRequestToTeam(request.POST)
    try:
        selectedPLayer = request.user.get_profile()
    except player.DoesNotExist:
        selectedPLayer = player(user=request.user)
    if delInvitation.is_valid():
        id = int(delInvitation.cleaned_data['team_id'])
        TeamReq = UserInTeamNtoN.objects.filter(team_id=id,user_id=selectedPLayer.pk)
        TeamReq[0].delete()
        return render_to_response('teams/messagePage.html',{'saved':True,'id_team':delInvitation.cleaned_data['team_id'],}, context_instance=RequestContext(request))
    else:
        return render_to_response('teams/messagePage.html',{'id_team':delInvitation.cleaned_data['team_id'],}, context_instance=RequestContext(request))

#Poslanie ziadosti do tímu
@login_required
def sendRequestForMembership(request):
    try:
        selectedPLayer = request.user.get_profile()
    except player.DoesNotExist:
        selectedPLayer = player(user=request.user)
    addInvitation = formularis.addRequestToTeam(request.POST)
    if addInvitation.is_valid():
        id = int(addInvitation.cleaned_data['team_id'])
        UserInTeamNtoNObject = UserInTeamNtoN(user_id=selectedPLayer,team_id=Team.objects.get(pk=id),invitation=True,dateOfAdd=datetime.datetime.now())
        UserInTeamNtoNObject.save()
        return render_to_response('teams/messagePage.html',{'saved':True,'id_team':addInvitation.cleaned_data['team_id'],}, context_instance=RequestContext(request))
    else:
        return render_to_response('teams/messagePage.html',{'id_team':addInvitation.cleaned_data['team_id'],}, context_instance=RequestContext(request))



#Zrušenie členstva v tíme
@login_required
def cancelMembership(request, pk):
    PK = int(pk)
    team = Team.objects.get(pk=PK)
    if request.method=='POST':
        try:
            selectedPLayer = request.user.get_profile()
        except player.DoesNotExist:
            selectedPLayer = player(user=request.user)
        delInvitation = formularis.deleteRequestToTeam(request.POST)
        if delInvitation.is_valid():
            membership = UserInTeamNtoN.objects.get(team_id=PK, user_id=selectedPLayer.pk)
            membership.delete()
            return render_to_response('teams/messageWarning.html',{'team':team,'saved':True,}, context_instance=RequestContext(request))
        else:
            return render_to_response('teams/messageWarning.html',{'team':team,'fail':True,}, context_instance=RequestContext(request))
    else:
        return render_to_response('teams/messageWarning.html',{'team':team,}, context_instance=RequestContext(request))



def teamDetail(request, pk):

    generalyTeamAdmin = None
    haveRequest = None
    haveRequetInThisTeam = None
    playerRequest = None
    team=None

    a = []
    PK = int(pk)

        #for e in UserInTeamNtoN.objects.filter(team_id=self.kwargs.get('pk', None)):
        #    a.append(player.objects.filter(pk=e.user_id.user_id)[0])
        #context['players'] = a

        #addInvitation = formularis.addRequestToTeam(request.POST)
        #delInvitation = formularis.deleteRequestToTeam(request.POST)

        #if addInvitation.is_valid():
        #    print addInvitation.cleaned_data['team_id']
        #if delInvitation.is_valid():
        #    print delInvitation.cleaned_data['team_id']
        #print 'Tu je add' , addInvitation
        #print 'Tu je del' , delInvitation
        #return render_to_response('teams/messagePage.html',None, context_instance=RequestContext(request))


    if request.method == 'GET':
        team = Team.objects.get(pk=PK)
        if request.user.is_authenticated():
            try:
                selectedPLayer = request.user.get_profile()
            except player.DoesNotExist:
                selectedPLayer = player(user=request.user)
            member = UserInTeamNtoN.objects.filter(user_id=selectedPLayer)
            teamadmin = Team.objects.filter(leader=selectedPLayer)


            if len(teamadmin) > 0:
                generalyTeamAdmin = True
                if teamadmin[0].pk == PK :
                    #je administratorom timu
                    return redirect('/teams/myTeam/')

            if len(member) > 0:
                haveRequest = True
                if member[0].team_id.pk == PK:
                    if member[0].accepted==True :
                        #je clen timu
                        return redirect('/teams/myTeam/')
                    elif member[0].invitation==True and member[0].accepted==False :
                        #Poziadavka bola odmietnuta
                        playerRequest = False
                        haveRequetInThisTeam = True
                    else:
                        #Poziadavka od hraca este nebola spracovana
                        playerRequest = True
                        haveRequetInThisTeam = True

        for e in UserInTeamNtoN.objects.filter(team_id=PK):
           a.append(player.objects.get(pk=e.user_id.pk))
        players = a

            #try:
            #    context['players'] = player(pk=UserInTeamNtoN(team_id=self.model.pk).user_id).objects.all()
            #except ValueError:
            #    print 'Error(Weak) - teams.views.DetailView - v danom time je len osoba ktora ho vytvorila'
            #    context['players'] = None

            #context['new_feeds'] = NewsFeeds(team_id=self.model.pk).objects.order_by('-publish_date')
        new_feeds= NewsFeeds.objects.filter(team_id=PK)
        GalleryTeam= Gallery.objects.filter(team_id=PK).order_by('date_of_add')

            #context['path'] = PROJECT_PATH.strip("\HrajAirsoft").replace('\\', '/') + "/"


        addRequestToTeam = formularis.addRequestToTeam(
            initial={'team_id': PK,}
        )

        deleteRequestToTeam = formularis.deleteRequestToTeam(
            initial={'team_id': PK,}
        )
        team_data = {
           'team':team,
           'new_feeds':new_feeds,
           'GalleryTeam':GalleryTeam,
           'playerRequest':playerRequest,
           'players':players,
           'teamadmin':generalyTeamAdmin,
           'addRequestToTeam':addRequestToTeam,
           'deleteRequestToTeam' :deleteRequestToTeam,
           'haveRequest':haveRequest,
           'haveRequetInThisTeam':haveRequetInThisTeam,
        }

        return render_to_response('teams/detail.html',team_data, context_instance=RequestContext(request))



@login_required
def addTeam(request):

    PlayerHasTeam = None
    saved = None
    if request.method == 'POST':

        form = addTeamForm(data=request.POST, files=request.FILES)

        if form.is_valid() and form.is_bound == True :

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            team_logo = form.cleaned_data['team_logo']
            big_logo = form.cleaned_data['big_logo']

            try:
                player = request.user.get_profile()
            except player.DoesNotExist:
                player = player(user=request.user)

            new_team = Team(name=name,description=description,team_logo=team_logo,big_logo=big_logo,counts_of_players=1,reg_date=datetime.datetime.now(),leader=player)

            new_team.save()
            saved = True

            return render_to_response('teams/addTeamForm.html', {'form': form, 'saved': saved, 'new':True }, context_instance=RequestContext(request))
        else:
            return render_to_response('teams/addTeamForm.html', {'form': form, 'fail': True, 'new':True }, context_instance=RequestContext(request))

    try:
        player = request.user.get_profile()
    except player.DoesNotExist:
        player = player(user=request.user)
    form = addTeamForm({})
    #if len(Team.objects.filter(leader=player))> 0 or len(UserInTeamNtoN.objects.filter(user_id=player)) > 0 :

    #admin
    if len(Team.objects.filter(leader=player))> 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'leader':True, 'PlayerHasTeam':PlayerHasTeam }, context_instance=RequestContext(request))
    #member
    if len(UserInTeamNtoN.objects.filter(user_id=player,accepted=True)) > 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'member':True, 'PlayerHasTeam':PlayerHasTeam }, context_instance=RequestContext(request))
    elif len(UserInTeamNtoN.objects.filter(user_id=player)) > 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'no_team':True, 'PlayerHasTeam':PlayerHasTeam }, context_instance=RequestContext(request))
    else:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'PlayerHasTeam':PlayerHasTeam }, context_instance=RequestContext(request))




@login_required
def myTeam(request):

    a = []
    try:
        playerObject = request.user.get_profile()
    except player.DoesNotExist:
        playerObject = player(user=request.user)

    team = UserInTeamNtoN.objects.filter(user_id=playerObject)

    #Je clen tímu, nie administrator
    if len(team) > 0:
        team = team[0]
        if team.accepted == True :
            team = Team.objects.get(pk=team.team_id.pk)
            for e in UserInTeamNtoN.objects.filter(team_id=team.pk):
                a.append(player.objects.get(pk=e.user_id.pk))
            new_feeds = NewsFeeds.objects.filter(team_id=team.pk)
            GalleryTeam = Gallery.objects.filter(team_id=team.pk)
            team_data = {'players': a, 'new_feeds': new_feeds,'GalleryTeam':GalleryTeam, 'team':team, 'isMember': True}
            return render_to_response('teams/detail.html', team_data, context_instance=RequestContext(request))

    #Ma poslanu ziadost do timu
        else:
            team2 = Team.objects.get(pk=team.team_id.pk)
            deleteRequestToTeam = formularis.deleteRequestToTeam(
            initial={'team_id': team.team_id.pk,}
            )
            team_data = { 'team':team2 , 'invitation':team , 'deleteRequestToTeam':deleteRequestToTeam }
            return render_to_response('players/myTeam.html',team_data, context_instance=RequestContext(request))

    teamadmin = Team.objects.filter(leader=playerObject)
    #Je administrator tímu
    if len(teamadmin) > 0 :
        for e in UserInTeamNtoN.objects.filter(team_id=teamadmin[0].pk):
            a.append(player.objects.get(pk=e.user_id.pk))
        new_feeds = NewsFeeds.objects.filter(team_id=teamadmin[0].pk)
        GalleryTeam = Gallery.objects.filter(team_id=teamadmin[0].pk)
        team_data = {'players': a, 'new_feeds': new_feeds,'GalleryTeam':GalleryTeam ,'team':teamadmin[0],'thisteamadmin':True}
        return render_to_response('teams/detail.html',team_data, context_instance=RequestContext(request))
    #Nema ziadny tím
    return render_to_response('players/myTeam.html', context_instance=RequestContext(request))


@login_required
def editBasicInfo(request,pk):

    PlayerHasTeam = None
    saved = None
    if request.method == 'POST':

        form = addTeamForm(data=request.POST, files=request.FILES)

        if form.is_valid() and form.is_bound == True :

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            team_logo = form.cleaned_data['team_logo']
            big_logo = form.cleaned_data['big_logo']

            try:
                player = request.user.get_profile()
            except player.DoesNotExist:
                player = player(user=request.user)
            editTeam = Team.objects.filter(leader=player.pk)[0]

            editTeam.name = name
            editTeam.description = description
            editTeam.team_logo = team_logo
            editTeam.big_logo = big_logo

            editTeam.save()
            saved = True

            return render_to_response('teams/addTeamForm.html', {'form': form, 'saved': saved , 'leader': True ,'edit':True,'pk':pk }, context_instance=RequestContext(request))
        else:
            return render_to_response('teams/addTeamForm.html', {'form': form, 'fail': True, 'edit':True,'pk':pk }, context_instance=RequestContext(request))

    try:
        player = request.user.get_profile()
    except player.DoesNotExist:
        player = player(user=request.user)
    editTeam = Team.objects.filter(leader=player.pk)[0]
    form = addTeamForm(initial={
        'name' : editTeam.name,
        'description' : editTeam.description,
        'team_logo' : editTeam.team_logo,
        'big_logo' : editTeam.big_logo,
        'last_name' : editTeam.name,
    })
    #if len(Team.objects.filter(leader=player))> 0 or len(UserInTeamNtoN.objects.filter(user_id=player)) > 0 :

    #admin
    if len(Team.objects.filter(leader=player))> 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'leader':True, 'PlayerHasTeam':PlayerHasTeam, 'edit':True,'pk':pk }, context_instance=RequestContext(request))
    #member
    if len(UserInTeamNtoN.objects.filter(user_id=player,accepted=True)) > 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'member':True, 'PlayerHasTeam':PlayerHasTeam ,'pk':pk}, context_instance=RequestContext(request))
    elif len(UserInTeamNtoN.objects.filter(user_id=player)) > 0:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'no_team':True, 'PlayerHasTeam':PlayerHasTeam ,'pk':pk}, context_instance=RequestContext(request))
    else:
        return render_to_response('teams/addTeamForm.html', {'form': form, 'PlayerHasTeam':PlayerHasTeam ,'pk':pk}, context_instance=RequestContext(request))


#Zmazanie tímu
@login_required
def deleteTeam(request, pk):
    PK = int(pk)
    team = Team.objects.get(pk=PK)
    if request.method=='POST':
        delTeam = formularis.deleteTeam(request.POST)
        if delTeam.is_valid():
            team.delete()
            return render_to_response('teams/messageWarning.html',{'team':team,'saved':True,'delTeam' : True}, context_instance=RequestContext(request))
        else:
            return render_to_response('teams/messageWarning.html',{'team':team,'fail':True,'delTeam' : True}, context_instance=RequestContext(request))
    else:

        form = formularis.deleteTeam(
            initial={'team_id': PK,}
        )
        return render_to_response('teams/messageWarning.html',{'form':form,'team':team, 'delTeam' : True}, context_instance=RequestContext(request))

