import { Component, Input } from '@angular/core';
import { Video } from '../../../../interfaces/video';

@Component({
  selector: 'app-video-player',
  standalone: true,
  imports: [],
  templateUrl: './video-player.component.html',
  styleUrl: './video-player.component.css'
})
export class VideoPlayerComponent {
  @Input() public url: string = '';
  @Input() public videoInfo: Video | null = null;
}
