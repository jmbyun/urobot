class URobotDrawer {
  constructor(containerElement) {
    this.containerElement = containerElement;
    this.walls = {};
    this.agents = {};
    this.markers = {};
    this.gridCells = {};
    this.initWorldElement();
  }

  // initWorld() {
  //   this.world = document.createElement('div');
  //   this.world.className = 'u-robot-drawer__world';
  //   this.container.appendChild(this.world);
  //   this.pieceElements = {};
  //   this.pieces = {};
  //   this.beeperElements = {};
  // }

  initWorldElement() {
    this.worldElement = document.createElement('div');
    this.worldElement.className = 'urobot-drawer__world';
    this.containerElement.appendChild(this.worldElement);
    return this.worldElement;
  }

  setWorldSize(width, height) {
    this.worldWidth = width;
    this.worldHeight = height;
    this.cellWidthPercentage = 100 / width;
    this.cellHeightPercentage = 100 / height;
    this.initGridCells();
    this.resize();
  }

  setWorldElementSize(width, height, paddingTop) {
    this.worldElement.style.width = `${width}px`;
    this.worldElement.style.height = `${height}px`;
    this.worldElement.style.paddingTop = `${paddingTop}px`;
  }

  initGridCells() {
    this.gridCells = {};
    for (let i = this.worldHeight - 1; i >= 0; i--) {
      this.gridCells[i] = {};
      const rowElement = document.createElement('div');
      rowElement.className = 'urobot-drawer__world-grid-row';
      rowElement.style.width = '100%';
      rowElement.style.height = `${this.cellHeightPercentage}%`;
      this.worldElement.appendChild(rowElement);
      for (let j = 0; j < this.worldWidth; j++) {
        const cellElement = document.createElement('div');
        this.gridCells[i][j] = cellElement;
        cellElement.className = 'urobot-drawer__world-grid-cell';
        cellElement.style.width = `${this.cellWidthPercentage}%`;
        cellElement.style.height = '100%';
        rowElement.appendChild(cellElement);
      }
    }
  }

  resize() {
    const containerWidth = this.containerElement.offsetWidth;
    const containerHeight = this.containerElement.offsetHeight;
    const cellSizeForWidthFit = containerWidth / this.worldWidth;
    const worldHeightForWidthFit = cellSizeForWidthFit * this.worldHeight;
    if (containerHeight > worldHeightForWidthFit) {
      this.scaleWorldWidthFit(containerWidth, containerHeight);
    } else {
      this.scaleWorldHeightFit(containerWidth, containerHeight);
    }
  }

  scaleWorldWidthFit(containerWidth, containerHeight) {
    const worldWidthPixels = containerWidth;
    const worldCellSize = worldWidthPixels / this.worldWidth;
    const worldHeightPixels = worldCellSize * this.worldHeight;
    const worldPaddingTop = (containerHeight - worldHeightPixels) / 2;
    this.setWorldElementSize(worldWidthPixels, worldHeightPixels, worldPaddingTop);
  }

  scaleWorldHeightFit(containerWidth, containerHeight) {
    const worldHeightPixels = containerHeight;
    const worldCellSize = worldHeightPixels / this.worldHeight
    const worldWidthPixels = worldCellSize * this.worldWidth;
    this.setWorldElementSize(worldWidthPixels, worldHeightPixels, 0);
  }


  // scaleWorld() {
  //   const containerWidth = this.container.offsetWidth;
  //   const containerHeight = this.container.offsetHeight;

  //   const cellSizeForWidthFit = containerWidth / this.worldWidth;
  //   const worldHeightForWidthFit = cellSizeForWidthFit * this.worldHeight;
  //   if (containerHeight > worldHeightForWidthFit) {
  //     this.scaleWorldWidthFit(containerWidth, containerHeight);
  //   } else {
  //     this.scaleWorldHeightFit(containerWidth, containerHeight);
  //   }
  // }

  // drawGrid() {
  //   this.cells = {}
  //   for (let i = this.worldHeight - 1; i >= 0; i--) {
  //     this.cells[i] = {};
  //     const row = document.createElement('div');
  //     row.className = 'u-robot-drawer__world-row';
  //     row.style.width = '100%';
  //     row.style.height = `${this.worldCellSize}px`;
  //     this.world.appendChild(row);
  //     for (let j = 0; j < this.worldWidth; j++) {
  //       const cell = document.createElement('div');
  //       this.cells[i][j] = cell;
  //       cell.className = 'u-robot-drawer__world-cell';
  //       cell.style.width = `${this.worldCellSize}px`;
  //       cell.style.height = `${this.worldCellSize}px`;
  //       row.appendChild(cell);
  //     }
  //   }
  // }

  // scaleWorldWidthFit() {
  //   const containerWidth = this.container.offsetWidth;
  //   const containerHeight = this.container.offsetHeight;
  //   const worldWidthPixels = containerWidth;
  //   this.worldCellSize = worldWidthPixels / this.worldWidth;
  //   const worldHeightPixels = this.worldCellSize * this.worldHeight;
  //   this.setWorldSize(worldWidthPixels, worldHeightPixels)
  //   const worldPaddingTop = (containerHeight - worldHeightPixels) / 2;
  //   this.world.style.paddingTop = `${worldPaddingTop}px`;
  // }

  // scaleWorldHeightFit() {
  //   const containerWidth = this.container.offsetWidth;
  //   const containerHeight = this.container.offsetHeight;
  //   const worldHeightPixels = containerHeight;
  //   this.worldCellSize = worldHeightPixels / this.worldHeight
  //   const worldWidthPixels = this.worldCellSize * this.worldWidth;
  //   this.setWorldSize(worldWidthPixels, worldHeightPixels)
  // }

  // setWorldSize(width, height) {
  //   this.world.style.width = `${width}px`;
  //   this.world.style.height = `${height}px`;
  // }

  // setPieceClasses(piece, pieceType, direction) {
  //   const classNames = [
  //     `u-robot-drawer__piece`,
  //     `u-robot-drawer__piece--type-${pieceType}`,
  //     `u-robot-drawer__piece--direction-${direction}`,
  //   ];
  //   piece.className = classNames.join(' ');
  // }

  // setPiecePosition(piece, x, y) {
  //   piece.style.left = `${this.worldCellSize * x}px`;
  //   piece.style.top = `${this.worldCellSize * (this.worldHeight - 1 - y)}px`;
  // }

  // getBeeperCount(x, y) {
  //   let count = 0;
  //   for (const piece of this.pieces) {
  //     if (piece.piece_type === 'beeper' && piece.x === x && piece.y === y) {
  //       count++;
  //     }
  //   }
  //   return count;
  // }

  // getBeeperElement(x, y) {
  //   let beeperElement = this.beeperElements[`${x},${y}`];
  //   if (!beeperElement) {
  //     beeperElement = document.createElement('div');
  //     beeperElement.style.width = `${this.worldCellSize}px`;
  //     beeperElement.style.height = `${this.worldCellSize}px`;
  //     this.setPiecePosition(beeperElement, x, y);
  //     this.world.appendChild(beeperElement);
  //     this.beeperElements[`${x},${y}`] = beeperElement;
  //   }
  //   return beeperElement;
  // }

  // refreshBeeperElement(x, y) {
  //   const beeperElement = this.getBeeperElement(x, y);
  //   const beeperCount = this.getBeeperCount(x, y);
  //   if (beeperCount > 0) {
  //     beeperElement.className = `u-robot-drawer__beeper`;
  //     beeperElement.innerHTML = beeperCount;
  //   } else {
  //     beeperElement.className = `u-robot-drawer__beeper u-robot-drawer__beeper--invisible`;
  //   }
  // }

  getCoordinatePercentage(x, y) {
    return {
      x: this.cellWidthPercentage * x,
      y: this.cellHeightPercentage * (this.worldHeight - y - 1),
    };
  }

  drawWall(x, y, direction) {
    const coordinate = this.getCoordinatePercentage(x, y);
    const wallElement = document.createElement('div');
    wallElement.className = [
      'urobot-drawer__wall',
      `urobot-drawer__wall--${direction}`,
    ].join(' ');
    const isVertical = direction === 'vertical';
    if (isVertical) {
      wallElement.style.height = `${this.cellHeightPercentage}%`;
    } else {
      wallElement.style.width = `${this.cellWidthPercentage}%`;
    }
    wallElement.style.left = `${coordinate.x}%`;
    wallElement.style.top = `${coordinate.y}%`;
    this.worldElement.appendChild(wallElement);
    this.walls[`${direction},${x},${y}`] = {
      direction: direction,
      x: x,
      y: y,
      element: wallElement,
    };
  }

  drawAgent(agent) {
    const coordinate = this.getCoordinatePercentage(agent.x, agent.y);
    const agentElement = document.createElement('div');
    agentElement.className = [
      'urobot-drawer__agent',
      `urobot-drawer__agent--type-${agent.agentType}`,
      `urobot-drawer__agent--direction-${agent.direction}`,
    ].join(' ');
    agentElement.style.width = `${this.cellWidthPercentage}%`;
    agentElement.style.height = `${this.cellHeightPercentage}%`;
    agentElement.style.left = `${coordinate.x}%`;
    agentElement.style.top = `${coordinate.y}%`;
    this.worldElement.appendChild(agentElement);
    this.agents[agent.id] = {
      ...agent,
      element: agentElement,
    };
  }

  removeAgent(agentId) {
    this.worldElement.removeChild(this.agents[agentId].element);
    delete this.agents[agentId];
  }

  moveAgent(agent) {
    const coordinate = this.getCoordinatePercentage(agent.x, agent.y);
    const agentElement = this.agents[agent.id].element;
    agentElement.style.left = `${coordinate.x}%`;
    agentElement.style.top = `${coordinate.y}%`;
    this.agents[agent.id] = {
      ...this.agents[agent.id],
      x: agent.x,
      y: agent.y,
    };
  }

  rotateAgent(agent) {
    const agentElement = this.agents[agent.id].element;
    agentElement.className = [
      'urobot-drawer__agent',
      `urobot-drawer__agent--type-${agent.agentType}`,
      `urobot-drawer__agent--direction-${agent.direction}`,
    ].join(' ');
    this.agents[agent.id] = {
      ...this.agents[agent.id],
      direction: agent.direction,
    };
  }

  getMarkerKey(marker) {
    return `${marker.markerType},${marker.x},${marker.y}`;
  }

  initMarkerCell(marker) {
    const markerKey = this.getMarkerKey(marker);
    if (!this.markers[markerKey]) {
      const coordinate = this.getCoordinatePercentage(marker.x, marker.y);

      const markerElement = document.createElement('div');
      markerElement.className = [
        'urobot-drawer__marker',
        `urobot-drawer__marker--type-${marker.markerType}`,
        `urobot-drawer__marker--invisible`,
      ].join(' ');
      markerElement.style.width = `${this.cellWidthPercentage}%`;
      markerElement.style.height = `${this.cellHeightPercentage}%`;
      markerElement.style.left = `${coordinate.x}%`;
      markerElement.style.top = `${coordinate.y}%`;

      const markerLabelElement = document.createElement('div');
      markerLabelElement.className = 'urobot-drawer__marker-label';
      markerElement.appendChild(markerLabelElement);

      this.worldElement.appendChild(markerElement);
      this.markers[markerKey] = {
        markers: [],
        element: markerElement,
        labelElement: markerLabelElement,
      };
    }
    return markerKey;
  }

  drawMarker(marker) {
    const markerKey = this.initMarkerCell(marker);
    const markers = this.markers[markerKey].markers;
    const markerElement = this.markers[markerKey].element;
    const markerLabelElement = this.markers[markerKey].labelElement;
    markers.push(marker);
    markerElement.classList.remove('urobot-drawer__marker--invisible');
    markerLabelElement.innerHTML = markers.length > 1 ? markers.length : '';
  }

  removeMarker(marker) {
    const markerKey = this.getMarkerKey(marker);
    const markerCell = this.markers[markerKey];
    if (!markerCell) {
      return;
    }
    markerCell.markers = markerCell.markers.fliter(m => m.id !== marker.id);
    if (markerCell.markers.length === 0) {
      markerCell.element.classList.add('urobot-drawer__marker--invisible');
    }
    markerCell.labelElement.innerHTML = markerCell.markers.length > 1 ? markers.length : '';
  }

  taskToAgent(task) {
    return {
      id: task.id,
      agentType: task.agent_type,
      x: task.x,
      y: task.y,
      direction: task.direction,
    };
  }

  taskToMarker(task) {
    return {
      id: task.id,
      markerType: task.marker_type,
      x: task.x,
      y: task.y,
    };
  }

  onDrawWorld(task) {
    this.setWorldSize(task.width, task.height);
  }

  onDrawWall(task) {
    if (task.x1 === task.x2) {
      if (Math.abs(task.y1 - task.y2) === 1) {
        this.drawWall(task.x1, Math.max(task.y1, task.y2), 'horizontal');
      }
    } else if (task.y1 === task.y2) {
      if (Math.abs(task.x1 - task.x2) === 1) {
        this.drawWall(Math.max(task.x1, task.x2), task.y1, 'vertical');
      }
    }
  }

  onDrawPiece(task) {
    if (task.piece_type === 'agent') {
      this.drawAgent(this.taskToAgent(task));
    } else if (task.piece_type === 'marker') {
      this.drawMarker(this.taskToMarker(task));
    }
  }

  onRemovePiece(task) {
    if (task.piece_type === 'agent') {
      this.removeAgent(task.id);
    } else if (task.piece_type === 'marker') {
      this.removeMarker(this.taskToMarker(marker));
    }
  }

  onMovePiece(task) {
    if (task.piece_type === 'agent') {
      this.moveAgent(this.taskToAgent(task));
    }
  }

  onRotatePiece(task) {
    if (task.piece_type === 'agent') {
      this.rotateAgent(this.taskToAgent(task));
    }
  }

  onTask(taskMessage) {
    const task = JSON.parse(taskMessage);
    console.log(task);
    switch (task.task) {
      case 'draw_world':
        this.onDrawWorld(task);
        break;

      case 'draw_wall':
        this.onDrawWall(task);
        break;

      case 'draw_piece':
        this.onDrawPiece(task);
        break;

      case 'remove_piece':
        this.onRemovePiece(task);
        break;

      case 'move_piece':
        this.onMovePiece(task);
        break;

      case 'rotate_piece':
        this.onRotatePiece(task);
        break;

      default:
        break;
    }
  }
}