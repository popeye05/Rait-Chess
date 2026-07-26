import { useState } from 'react'
import { Chessboard } from 'react-chessboard'
import { Chess } from 'chess.js'

function App() {
  const [game, setGame] = useState(new Chess())
  const [coaching, setCoaching] = useState('')

  async function getCoaching(fenBeforeMove, userMoveSan) {
    const response = await fetch('http://127.0.0.1:8000/analyze-move', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        fen: fenBeforeMove,
        user_move: userMoveSan,
      }),
    })

    const data = await response.json()
    setCoaching(data.coaching)
  }

  function onPieceDrop({ sourceSquare, targetSquare }) {
    const fenBeforeMove = game.fen()
    const gameCopy = new Chess(fenBeforeMove)

    try {
      const move = gameCopy.move({
        from: sourceSquare,
        to: targetSquare,
        promotion: 'q',
      })

      if (move === null) {
        return false
      }

      setGame(gameCopy)
      getCoaching(fenBeforeMove, move.san)

      return true
    } catch (error) {
      return false
    }
  }

  function handleReset() {
    setGame(new Chess())
    setCoaching('')
  }

  const chessboardOptions = {
    position: game.fen(),
    onPieceDrop: onPieceDrop,
  }

  const turnLabel = game.turn() === 'w' ? 'White' : 'Black'

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '20px',
      }}
    >
      <h1>Rait Chess</h1>

      <p style={{ fontSize: '18px', marginBottom: '10px' }}>
        {turnLabel} to move
      </p>

      <div style={{ width: '400px' }}>
        <Chessboard options={chessboardOptions} />
      </div>

      <button onClick={handleReset} style={{ marginTop: '15px' }}>
        Reset Game
      </button>

      <p style={{ maxWidth: '500px', textAlign: 'center', marginTop: '20px' }}>
        {coaching}
      </p>
    </div>
  )
}

export default App