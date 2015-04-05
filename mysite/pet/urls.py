from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
        url(
            r'^display/$',
            'pet.views.Display',
            name = 'Display'

        ),
        url(
            r'^picture/$',
            'pet.views.PictureCreator',
            name = 'PictureCreator'
        ),
        url(r'^board/$',
            'pet.views.BoardCreator',
            name = 'BoardCreator'
        ),
	url(
	    r'^register/$',
	    'pet.views.PetRegistration',
	    name = 'PetRegistration'
        ),
	
	url(
	    r'^login/$',
	    'pet.views.LoginRequest',
	    name = 'LoginRequest'
	),
	
	url(
	    r'^logout/$',
	    'pet.views.LogoutRequest',
	    name = 'LogoutRequest'
	),
	url(
	    r'^profile/(?P<slug>[-\w\d]+)/$',
	    'pet.views.Profile',
	    name = 'Profile'
	),


    url(
        r'^friend/add/(?P<to_username>[\w-]+)/$',
        'pet.views.friendship_add_friend',
        name='friendship_add_friend',
    ),

    url(
        r'^follower/add/(?P<followee_username>[\w-]+)/$',
        'pet.views.follower_add',
        name='follower_add',
    ),

        url(
            r'^archive/$',
            'pet.views.archive',
            name = 'archive'
        ),


        url(r'^board/(?P<slug>[-\w\d]+),(?P<id>\d+)/(?P<picture_id>\d+)$', 
            'pet.views.description',
            name ='description'
        ),


    
        url(
            r'^following/$',
            'pet.views.Follower',
            name = 'Follower'
        ),

        url(
            r'^boardfinder/$',
            'pet.views.BoardFinder',
            name = 'BoardFinder'
        ),


        url(
            r'^boardeditor/$',
            'pet.views.BoardEditor',
            name = 'BoardEditor',
        ),

        url(
            r'^changepicture/(?P<picture_id>\d+)/$',
            'pet.views.ChangePicture',
            name= 'ChangePicture',
        ),

        url(
            r'following/(?P<slug>[-\w\d]+)/cancelfriend/$',
            'pet.views.CancelFriend',
            name = 'CancelFriend'
        ),
        url(r'following/(?P<slug>[-\w\d]+)/addfriend/$',
            'pet.views.AddFriend',
            name = 'AddFriend'
        ),
        url(
            r'^Myfriend/$',
            'pet.views.Myfriend',
            name= 'Myfriend',
        ),
        url(
            r'^Follow/$',
            'pet.views.Following',
            name= 'Following',
        ),
        url(
            r'^sparkprofile/$',
            'pet.views.Sparkprofile',
            name = 'Sparkprofile',
        ),

        url(
            r'^SearchPerson/$',
            'pet.views.SearchPerson',
            name = 'SearchPerson',
        ),                 




        url(
            r'^followingall/$',
            'pet.views.FollowingAll',
            name = 'FollowingAll',
        ),   

  


        url(
            r'^whatisparkalight/$',
            'pet.views.whatspark',
            name = 'whatspark',
        ),

        url(
            r'^contact/$',
            'pet.views.Contacts',
            name = 'contact',
        ),

        url(
            r'^EditFriend/$',
            'pet.views.EditFriend',
            name = 'EditFriend',
        ),
        url(
            r'^friendstar/(?P<slug>[-\w\d]+)/$',
            'pet.views.friendstar',
            name = 'friendstar',
        ),   

        url(
            r'^term-and-condition/$',
            'pet.views.term',
            name = 'term',
        ),

        url(
            r'^privacy-policy/$',
            'pet.views.privacy',
            name = 'privacy',
        ),        

        url(
            r'^faq/$',
            'pet.views.Faq',
            name = 'faq',
        ),        


        url(r'car/like$', 'pet.views.like', name = 'like' ),
        url(r'car/postComment$', 'pet.views.post_comment', name = 'post_comment' ),
		url(r'car/getComment$', 'pet.views.get_comment', name = 'get_comment' ),
		url(r'car/deleteComment$', 'pet.views.delete_comment', name = 'delete_comment' ),
        

        url(
            r'^board/(?P<slug>[-\w\d]+),(?P<id>\d+)/$',
            'pet.views.Car',
            name = 'Car',

        ),
	url(
            r'car/search$',
            'pet.views.BoardFinder',
            name = 'search'
        ),
	url(
            r'car/searchBoards$',
            'pet.views.search_boards',
            name = 'search_boards'
        ),



    url(
            r'^friend/accept/(?P<friendship_request_id>\d+)/$',
            'pet.views.friendship_accept',
            name='friendship_accept',
    ),    


    url(
        r'^friend/cancelss/(?P<username>[\w-]+)/$',
        'pet.views.friendship_cancel',
        name='friendship_cancel',
    ),

    url(
        r'^follower/remove/(?P<followee_username>[\w-]+)/$',
        'pet.views.follower_remove',
        name='follower_remove',
    ),
    url(
        r'^friend/remove/(?P<friendship_request_id>\d+)/$',
        'pet.views.friendship_reject',
        name='friendship_reject',
    ),



)
                       


