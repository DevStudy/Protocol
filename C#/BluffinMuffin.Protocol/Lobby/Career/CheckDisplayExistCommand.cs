﻿namespace BluffinMuffin.Protocol.Lobby.Career
{
    public class CheckDisplayExistCommand : AbstractLobbyCommand, ICommandWithResponse<CheckDisplayExistResponse>
    {
        public string DisplayName { get; set; }

        public CheckDisplayExistResponse Response(bool exist)
        {
            return new CheckDisplayExistResponse(this) { Exist = exist };
        }
    }
}
