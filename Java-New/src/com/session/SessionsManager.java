package com.session;

public class SessionsManager {
    /**
     * This will control, save and manage all sessions that we wish to switch between
      */

    Session activeSession;

    public SessionsManager(){
        activeSession = new Session();
    }
}
