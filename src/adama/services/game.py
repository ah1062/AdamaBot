import logging

from adama.repositories.game import game_repo

logger = logging.getLogger(__name__)

class GameService:
	def __init__(self, repo) -> None:
		logger.info(repo.conn)

game_service = GameService(game_repo)
