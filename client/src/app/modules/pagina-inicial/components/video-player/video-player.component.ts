import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { Video } from '../../../../interfaces/video';

@Component({
  selector: 'app-video-player',
  standalone: true,
  imports: [],
  templateUrl: './video-player.component.html',
  styleUrl: './video-player.component.css'
})
export class VideoPlayerComponent implements OnChanges{
  @Input() public url: string = '';
  @Input() public videoInfo: Video | null = null;

  ngOnChanges(changes: SimpleChanges): void {
    console.log("URL TO PLAY", this.url);
  }
}
